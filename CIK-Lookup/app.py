import requests

class SecEdgar:
    def __init__(self, fileurl):
        self.fileurl = fileurl

        headers = {'user-agent': 'MLT KC kcao5@vols.utk.edu'}
        r = requests.get(self.fileurl, headers=headers)

        self.filejson = r.json()
        self.cik_json_to_dict()
        
    def cik_json_to_dict(self):
        self.name_dict = {}
        self.ticker_dict = {}

        for entry in self.filejson.values():
            cik = entry['cik_str']
            ticker = entry['ticker']
            name = entry['title']

            self.name_dict[name.lower()] = (cik, ticker, name)
            self.ticker_dict[ticker.lower()] = (cik, ticker, name)    

    def name_to_cik(self, name):
        return self.name_dict.get(name.lower())
    
    def ticker_to_cik(self, ticker):
        return self.ticker_dict.get(ticker.lower())


se = SecEdgar("https://www.sec.gov/files/company_tickers.json")
print (se.name_to_cik("TORONTO DOMINION BANK"))
print (se.ticker_to_cik("FTNT"))