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
import pandas_datareader.data as wb

#Functions


def removeDifferentDates(df1, df2, columnName1, columnName2):
    dates1 = list(df1.index)
    dates2 = list(df2.index)
    
    i = 0

    while i < len(dates1):
        if type(dates2[i]) is datetime:
            dates1[i] = str(dates1[i].date().strftime('%m-%d-%Y'))
        i = i + 1

    i = 0

    while i < len(dates2):
        if type(dates2[i]) is datetime:
            dates2[i] = str(dates2[i].date().strftime('%m-%d-%Y'))
        i = i + 1

    index = 0

    toRemoveFrom2 = []

    while index < len(dates2):
        checkIndex = 0
        found = False
        while checkIndex < len(dates1):
            if dates1[checkIndex] == dates2[index]:
                found = True
            checkIndex = checkIndex + 1
        if found == False:
            toRemoveFrom2.append(index)
        index = index + 1

    index = 0

    toRemoveFrom1 = []

    while index < len(dates1):
        checkIndex = 0
        found = False
        while checkIndex < len(dates2):
            if dates2[checkIndex] == dates1[index]:
                found = True
            checkIndex = checkIndex + 1
        if found == False:
            toRemoveFrom1.append(index)
        index = index + 1

    removeIndex = 0

    print(len(toRemoveFrom1))
    if len(toRemoveFrom1) > 0:
        while removeIndex < len(toRemoveFrom1):
            r = toRemoveFrom1[removeIndex]
            dates1.remove(dates1[r])
            removeIndex = removeIndex + 1

    #dates1 list is modified
    
    var1 = df1[columnName1].values.tolist()

    removeIndex = 0

    if len(toRemoveFrom1) > 0:
        while removeIndex < len(toRemoveFrom1):
            r = toRemoveFrom1[removeIndex]
            var1.remove(var1[r])
            removeIndex = removeIndex + 1

    #var1 list is modified
            
    removeIndex = 0

    if len(toRemoveFrom2) > 0:
        while removeIndex < len(toRemoveFrom2):
            r = toRemoveFrom2[removeIndex]
            dates2.remove(dates2[r])
            removeIndex = removeIndex + 1

    #dates2 list is modified
            
    var2 = df2[columnName2].values.tolist()

    removeIndex = 0

    if len(toRemoveFrom2) > 0:
        while removeIndex < len(toRemoveFrom2):
            r = toRemoveFrom2[removeIndex]
            var2.remove(var2[r])
            removeIndex = removeIndex + 1

    #var2 list is modified
            
    retdf1 = pd.DataFrame({'Date': dates1, columnName1: var1})
    retdf2 = pd.DataFrame({'Date': dates2, columnName2: var2})

    retdf1 = retdf1.set_index('Date')
    retdf2 = retdf2.set_index('Date')
    
    final = [retdf1, retdf2]

    return final

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

print(VIX_df)

print(skewdf)


#print(VIX_df.columns.values)

l = removeDifferentDates(skewdf, VIX_df, 'Skew', 'VIX')

print(skewdf.index == VIX_df.index)

#CONVERT Y/M/D TO Y-M-D
