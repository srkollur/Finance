import quandl
import numpy as np
import scipy
import matplotlib.pyplot as plt
import xlsxwriter
import pandas as pd
import yahoo_finance
from yahoo_finance import Share
import datetime
from datetime import datetime
import statistics
import pandas_datareader.data as data

#Functions


def removeDifferentDates(df1, df2):
    dates1 = list(df1.index)
    dates2 = list(df2.index)
    
    i = 0

    while i < len(dates2):
        dates2[i] = dates2[i].date().strftime('%Y-%m-%d')
        i = i + 1

    index = 0

    while index < len(dates1):
        dates1[index] = datetime.strptime(dates1[index], "%m/%d/%Y").strftime("%Y-%m-%d")
        index = index + 1

    index = 0

    print('test')
    
    df1.index = dates1
    df2.index = dates2

    print('test1')
    
    overallIndexes = list(set(dates1).intersection(set(dates2)))

    print(len(overallIndexes))

    checkIndex = 0

    df1 = df1[df1.index.isin(overallIndexes)]
    df2 = df2[df2.index.isin(overallIndexes)]
    
    print(len(df1))
    print(len(df2))

    return [df1, df2]

skewdf = quandl.get("CBOE/SKEW", authtoken="HMbMEXCjrykoHnyB6PVC", start_date = "2006-12-13", end_date = "2017-08-24")

VIXurl = 'http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/vixcurrent.csv'
VIX_df = pd.DataFrame(pd.read_csv(VIXurl))

VIX_values = VIX_df["Unnamed: 4"].tolist()

VIX_values.remove(VIX_values[0])

series = (VIX_df["CBOE data is compiled for the convenience of site visitors and is furnished without responsibility for accuracy and is accepted by the site visitor on the condition that transmission or omissions shall not be made the basis for any claim demand or cause for action.  Your use of CBOE data is subject to the Terms and Conditions of CBOE's Websites."])

VIX_list = series.values.tolist()

label = VIX_list[0]

VIX_list.remove(VIX_list[0])

VIX_df = pd.DataFrame({label: VIX_list, "VIX": VIX_values})

VIX_df = VIX_df.set_index('Date')


l = removeDifferentDates(VIX_df, skewdf)

VIXdf = l[0]
skewdf = l[1]

print(skewdf.index == VIXdf.index)


