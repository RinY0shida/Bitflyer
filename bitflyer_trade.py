import pybitflyer
import requests

class BitflyerTrade:
    # @brief コンストラクタ
    # @param api_key APIキー
    # @param api_secret APIシークレット
    def __init__(self, api_key, api_secret):
        self.api = pybitflyer.API(api_key, api_secret)

    # @brief 成り行き買い注文
    # @param amount 注文数量(BTC)
    # @param expiration_time 有効期限(minute)
    def BuyMkt(self, amount, expiration_time):
        amount = int(amount*100000000)/100000000
        buy = self.api.sendchildorder(product_code = "BTC_JPY", child_order_type = "MARKET", side = "BUY", amount = amount, minute_to_expire = expiration_time, time_in_force = "GTC")
        print("BuyMkt: ", amount)
        print(buy)

    # @brief 成り行き売り注文
    # @param amount 注文数量(BTC)
    # @param expiration_time 有効期限(minute)
    def SellMkt(self, amount, expiration_time):
        amount = int(amount*100000000)/100000000
        sell = self.api.sendchildorder(product_code = "BTC_JPY", child_order_type = "MARKET", side = "SELL", amount = amount, minute_to_expire = expiration_time, time_in_force = "GTC")
        print("SellMkt: ", amount)
        print(sell)

    # @brief 指値買い注文
    # @param amount 注文数量(BTC)
    # @param price 注文価格(JPY)
    # @param expiration_time 有効期限(minute)
    def BuyLmt(self, amount, price, expiration_time):
        amount = int(amount*100000000)/100000000
        price = int(price)
        buy = self.api.sendchildorder(product_code = "BTC_JPY", child_order_type = "LIMIT", side = "BUY", price = price, amount = amount, minute_to_expire = expiration_time, time_in_force = "GTC")
        print("BuyLmt: ", amount, price)
        print(buy)

    # @brief 指値売り注文
    # @param amount 注文数量(BTC)
    # @param price 注文価格(JPY)
    # @param expiration_time 有効期限(minute)
    def SellLmt(self, amount, price, expiration_time):
        amount = int(amount*100000000)/100000000
        price = int(price)
        sell = self.api.sendchildorder(product_code = "BTC_JPY", child_order_type = "LIMIT", side = "SELL", price = price, amount = amount, minute_to_expire = expiration_time, time_in_force = "GTC")
        print("SellLmt: ", amount, price)
        print(sell)

    def GetAccountInformation(self):
        account = self.api.getbalance()
        print(account)
