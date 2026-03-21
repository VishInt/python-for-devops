import requests

API_KEY = "F1OVBF8KHFSVZYB2"                     # step1 get API Key

api_url = "https://www.alphavantage.co/"         # step2 find a base URL

symbol = "AMZN"
interval = "5min"

# query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&interval=5min&apikey={API_KEY}"


# print(api_url+query)

def get_stock_market_data(symbol):
    if is_timeseries:
        query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&interval=5min&apikey={API_KEY}"
    else:
        query = f"query?symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url=api_url+query)

    for key, value in response.json().items():
        # if key == "Time Series (Daily)":
        # if key == "Meta Data":
        if is_timeseries:
            # if key == "Time Series (Daily)":
            #     continue
            print(key,value)
        else:
            if key == "Time Series (Daily)":
                continue
    # print(response.json())

symbol = input("Enter the symbol you want for the stock Market API eg. (AMZN, GOGL, IBM, etc)")
is_timeseries = True
get_stock_market_data(symbol)