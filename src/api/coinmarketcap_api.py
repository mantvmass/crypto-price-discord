from requests import Session
import keys
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class api_checking:
  def __init__(self):
    self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    self.headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': keys.api_key_coinmarketcap,
    }
    self.session = Session()
    self.session.headers.update(self.headers)
    self.pt_u1 = {
      'start':'1',
      'limit':'5000',
      'convert':'USD'
    }
    self.pt_u2 = {
      'start':'5001',
      'limit':'10000',
      'convert':'USD'
    }
    self.pt_u3 = {
      'start':'10001',
      'limit':'15000',
      'convert':'USD'
    }
    try:
      response1 = self.session.get(self.url, params=self.pt_u1)
      data1 = json.loads(response1.text)

      response2 = self.session.get(self.url, params=self.pt_u1)
      data2 = json.loads(response2.text)

      response3 = self.session.get(self.url, params=self.pt_u1)
      data3 = json.loads(response3.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    self.coins1 = data1['data']
    self.coins2 = data2['data']
    self.coins3 = data3['data']


  def get_price_usd(self,check):

    for x in self.coins1:
      if x['symbol'] == check.upper():
        print(x['symbol'], x['quote']['USD']['price'])
        return x['quote']['USD']['price']
    for x in self.coins2:
      if x['symbol'] == check.upper():
        print(x['symbol'], x['quote']['USD']['price'])
        return x['quote']['USD']['price']


# p = api_checking()
# p.get_price_usd("vrsc")
