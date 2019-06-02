import requests

def get_stock_quotes():

    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=H24.F&apikey=SK4NCW73RJ7NRIUV"
    data = requests.get(url).json()
    name = "home 24 SE"
    stocks_name = data["Meta Data"]["2. Symbol"]
    currency = "Frankfurt. Currency in EUR"
    from_to_date = "Time Period: May 27, 2019 - May 31, 2019"
    time_period = [data["Time Series (Daily)"]["2019-05-27"]["1. open"],
                   data["Time Series (Daily)"]["2019-05-28"]["1. open"],
                   data["Time Series (Daily)"]["2019-05-29"]["1. open"],
                   data["Time Series (Daily)"]["2019-05-30"]["1. open"],
                   data["Time Series (Daily)"]["2019-05-31"]["1. open"]
                   ]
    weekdays = ["Mo ", " Tu ", " We ", " Th ", " Fr "]
    complete_data = name + " (" + stocks_name + ")" + "\n" + currency + "\n" + from_to_date + "\n" + "\n" + \
                    weekdays[0] + " " + weekdays[1] + " " + weekdays[2] + " " + weekdays[3] + " " + weekdays[4] + "\n" +\
                    time_period[0][0:4] + " " + time_period[1][0:4] + " " + time_period[2][0:4] + " " + time_period[3][0:4] + " " + time_period[4][0:4]
    print(complete_data)

get_stock_quotes()

