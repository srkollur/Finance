import pandas as pd
import io
import requests
import time
 
##def google_stocks(symbol, startdate = (1, 1, 2005), enddate = None):
## 
##    startdate = str(startdate[0]) + '+' + str(startdate[1]) + '+' + str(startdate[2])
## 
##    if not enddate:
##        enddate = time.strftime("%m+%d+%Y")
##    else:
##        enddate = str(enddate[0]) + '+' + str(enddate[1]) + '+' + str(enddate[2])
## 
##    stock_url = "http://www.google.com/finance/historical?q=" + symbol + \
##                "&startdate=" + startdate + "&enddate=" + enddate + "&output=csv"
## 
##    raw_response = requests.get(stock_url).content
## 
##    stock_data = pd.read_csv(io.StringIO(raw_response.decode('utf-8')))
##
##    print(type(stock_data))
##    return stock_data
## 
## 
##if __name__ == '__main__':
##    apple_data = google_stocks('AAPL')
##    print(apple_data)
## 
##    apple_truncated = google_stocks('AAPL', enddate = (1, 1, 2006))
##    #print(apple_truncated)

import datetime
from pandas_datareader import data

symbol = 'AAPL'
start = datetime.datetime(2006, 12, 14) # as example
end = datetime.datetime(2007, 12, 14)

#Unfortunately the google version of the following only returns 1 year:
stock_data = data.get_data_yahoo(symbol, start, end)

lis = stock_data.index.tolist()

df = pd.DataFrame({'Date': lis})

print(df)

