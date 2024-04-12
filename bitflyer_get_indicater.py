import requests
import time
import json
import matplotlib.pyplot as plt


def prev_response():

    pull_amount = 51

    prev_data = [0] * pull_amount

    prev_open = [0] * pull_amount
    prev_high = [0] * pull_amount
    prev_low = [0] * pull_amount
    prev_close = [0] * pull_amount
    prev_top = [0] * pull_amount
    prev_down = [0] * pull_amount

    prev_response = requests.get("https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=JPY&limit=50")  #1日分の分足を取得

    prev_response = prev_response.json()
    stock_data = prev_response["Data"]["Data"]

    count = 0
    for i in stock_data:
        prev_data[count] = stock_data[count]

        prev_open[count] = prev_data[count]["open"]
        prev_high[count] = prev_data[count]["high"]
        prev_low [count]= prev_data[count]["low"]
        prev_close[count] = prev_data[count]["close"]

        if prev_open[count] < prev_close[count]:

            prev_top[count] = prev_close[count]
            prev_down[count] = prev_open[count]
            
        else:
            prev_top[count] = prev_open[count]
            prev_down[count] = prev_close[count]

        

        print("Open{0} , High{1} , Low{2} , Close{3}" .format(prev_open[count] , prev_high[count] , prev_low[count] , prev_close[count]))


        count = count + 1

    plt.plot(prev_top , color = 'g')
    plt.plot(prev_down , color = 'y')
    plt.plot(prev_high , color = 'r')
    plt.plot(prev_low , color = 'b')
    plt.show()

while(60):
    prev_response()




# while(1):
#     time.sleep(60)
#     response = requests.get("https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=JPY&limit=1")
#     #print(response.json())
#     response = response.json()

#     data = response["Data"]["Data"][0]
#     data_open = data["open"]
#     data_high = data["high"]
#     data_low = data["low"]
#     data_close = data["close"]


#     print("Open{0} , High{1} , Low{2} , Close{3}" .format(data_open , data_high , data_low , data_close))

    
