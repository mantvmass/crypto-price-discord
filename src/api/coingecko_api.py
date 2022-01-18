from pycoingecko import CoinGeckoAPI

class check_push:
    def __init__(self):
        self.coin_list = ["btc","vrsc", "kub"]
        self.coin_check  = ["bitcoin",  "verus-coin", "bitkub-coin"]
        self.check_coins = CoinGeckoAPI()
        if len(self.coin_list) != len(self.coin_check):
            print("Value index not match!")
            return None

    def usd(self, symbol):
        num = 0
        for x in self.coin_list:
            if symbol.upper() == x.upper():
                c = self.check_coins.get_price(ids=self.coin_check[num], vs_currencies='usd')
                return c[self.coin_check[num]]['usd'], "USD"
            num += 1
        return "not find!"

    def thb(self, symbol):
        num = 0
        for x in self.coin_list:
            if symbol.upper() == x.upper():
                c = self.check_coins.get_price(ids=self.coin_check[num], vs_currencies='thb')
                return c[self.coin_check[num]]['thb'], "THB"
            num += 1
        return "not find!"


# o=check_push()
# oo=o.usd("hhh")
# print(oo)
# o = check_coins.get_price(ids='verus-coin',vs_currencies='thb')
# print(o['verus-coin']['thb'])
