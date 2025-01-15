import json
import matplotlib.pyplot as plt
from bitcoin_ohcl_fetcher import BitcointOhclFetcher
from bitflyer_trade import BitflyerTrade

# @brief APIキーを取得する
# @param file_name APIキーが記載されたファイル名
# @return APIキーとAPIシークレットが記載された辞書型データ

def GetApiKey(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def main():
    bitcoin_ohcl_fetcher = BitcointOhclFetcher()
    
    minute_ohcl_result = bitcoin_ohcl_fetcher.FetchOhclData("histominute", "1999")
    #print(f"取得した分速データの個数: {len(minute_ohcl_result)}個")
    #print(minute_ohcl_result[:2000])
    
    minute_close = [data["close"] for data in minute_ohcl_result]
    minute_average = sum(minute_close) / len(minute_close)

    print(minute_average)
    
    # plt.plot(minute_close, color = 'k')
    # plt.show()


    key_data = GetApiKey("bitflyer_api_key.json")
    print(key_data["api_key"])
    print(key_data["api_secret"])

    bitflyer_trade = BitflyerTrade(key_data["api_key"], key_data["api_secret"])
    bitflyer_trade.GetAccountInformation()



    # init() 初期化関数を将来的に呼び出すようにしたい。

    # while True:
        # 

if __name__ == "__main__":
    main()
