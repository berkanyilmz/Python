import requests

class Api:

  def __init__(self):
    self.api_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    self.api_key = "your api key"
    self.parameters = {
        'start':'1',
        'limit':'500',
        'convert':'USD'}
    self.headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': self.api_key}

    self.session = requests.Session()
    self.session.headers.update(self.headers)

  def get_response(self):
    self.response = self.session.get(self.api_url, params=self.parameters)
    self.json_data = self.response.json()
    return self.json_data


#print(json_data['data'][0]['symbol'])
#coin bulma
#for i in range(100):
#    if (json_data['data'][i]['symbol'] == 'LEO'):
#        print(json_data['data'][i])
