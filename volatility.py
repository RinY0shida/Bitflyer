import pandas as pd
import numpy as np
import requests

daily_amount = 2000
hourly_amount = 2000
minute_amount = 2000


def miniutu_ohlc():
    response = requests.get("https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=JPY&limit=2000")
    stock_data = response.json()["Data"]["Data"]

    data_list = []

    for data in stock_data:
        data_list.append({
            "open": data["open"],
            "high": data["high"],
            "low": data["low"],
            "close": data["close"]
        })
    return data_list


def hourly_ohlc():
    response = requests.get("https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=JPY&limit=2000")
    stock_data = response.json()["Data"]["Data"]

    data_list = []

    for data in stock_data:
        data_list.append({
            "open": data["open"],
            "high": data["high"],
            "low": data["low"],
            "close": data["close"]
        })
    return data_list


def daily_amount():
    response = requests.get("https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=JPY&limit=2000")
    stock_data = response.json()["Data"]["Data"]

    data_list = []

    for data in stock_data:
        data_list.append({
            "open": data["open"],
            "high": data["high"],
            "low": data["low"],
            "close": data["close"]
        })
    return data_list



miniutu_ohlc_result = miniutu_ohlc()
hourly_ohlc_result = hourly_ohlc()
daily_amount_result = daily_amount()

#print(f"取得したデータの個数: {len(miniutu_ohlc_result)}個")
#print(f"取得したデータの個数: {len(hourly_ohlc_result)}個"
#print(f"取得したデータの個数: {len(daily_amount_result)}個")


for i, data in enumerate(result[:2001]):
    print(f"Data {i}: Open {data['open']}, High {data['high']}, Low {data['low']}, Close {data['close']}")









