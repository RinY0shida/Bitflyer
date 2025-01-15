import pandas as pd
import numpy as np
import requests

class BitcointOhclFetcher:
    
    # @brief OHCLデータを取得する
    # @param interval 取得するOHCLデータの間隔 (histominute, histohour, histoday)
    # @param num 取得するOHCLデータの個数
    # @return OHCLデータのリスト
    def FetchOhclData(self, interval, num):
        url = f"https://min-api.cryptocompare.com/data/v2/{interval}?fsym=BTC&tsym=JPY&limit={num}"
        response = requests.get(url)
    
        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code}")
            return []
    
        stock_data = response.json()["Data"]["Data"]
    
        data_list = [{
            "open": data["open"],
            "high": data["high"],
            "low": data["low"],
            "close": data["close"]
        } for data in stock_data]
    
        return data_list

# # 各タイムフレームのデータを取得
# minute_ohlc_result = get_ohlc_data("histominute")
# hourly_ohlc_result = get_ohlc_data("histohour")
# daily_ohlc_result = get_ohlc_data("histoday")

# # データの個数を表示
# print(f"取得した分足データの個数: {len(minute_ohlc_result)}個")
# print(f"取得した時足データの個数: {len(hourly_ohlc_result)}個")
# print(f"取得した日足データの個数: {len(daily_ohlc_result)}個")

# for i, data in enumerate(minute_ohlc_result[:2001]):
#     print(f"Data {i}: Open {data['open']}, High {data['high']}, Low {data['low']}, Close {data['close']}")

# for i, data in enumerate(hourly_ohlc_result[:2001]):
#     print(f"Data {i}: Open {data['open']}, High {data['high']}, Low {data['low']}, Close {data['close']}")

# for i, data in enumerate(daily_ohlc_result[:2001]):
#     print(f"Data {i}: Open {data['open']}, High {data['high']}, Low {data['low']}, Close {data['close']}")
