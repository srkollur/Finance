import quandl
import numpy as np
import scipy
import matplotlib.pyplot as plt
import xlsxwriter
import pandas as pd
import xlrd

xl = pd.ExcelFile("Data File_Dirty.xlsx")
xl.sheet_names

df = xl.parse("Sheet1")

IPCRatio = df['Index P/C Ratio'].tolist()
PCRatio = df['P/C Ratio'].tolist()
Close = df['Close'].tolist()
VIXClose = df['VIX Close'].tolist()
IWMClose = df['IWM Close'].tolist()
TLTClose = df['TLT Close'].tolist()
XLPClose = df['XLP Close'].tolist()
GLD = df['GLD'].tolist()

#df = df.head()

#df = df['Variance_Weighted']

#dfList = df['Convert'].tolist()

finalList = []

#print(IPCRatio)

print(type(IPCRatio[0]))

def mod(dfList):
    i = 30
    length = len(dfList)
    newList = []
    while(i < length):
        total = 0.0
        countIndex = i-30
        while(countIndex < i):
            #print(IPCRatio[countIndex])
            #print(type(dfList[countIndex]))
            #print(type(total))
            if type(dfList[countIndex]) is float:
                total = total + dfList[countIndex]
            countIndex = countIndex + 1
        average = total/30
        #print(average)
        newList.append(average)
        i = i + 1
    return newList

IPCRatio = mod(IPCRatio)
#print(IPCRatio)
PCRatio = mod(PCRatio)
Close = mod(Close)
VIXClose = mod(VIXClose)
IWMClose = mod(IWMClose)
TLTClose = mod(TLTClose)
XLPClose = mod(XLPClose)
GLD = mod(GLD)

finaldf = pd.DataFrame({'Index P/C Ratio': IPCRatio, 'P/C Ratio': PCRatio, 'Close': Close, 'VIX Close': VIXClose,'IWM Close': IWMClose, 'TLT Close': TLTClose, 'XLP Close': XLPClose, 'GLD': GLD})

writer = pd.ExcelWriter('Clean Data_1.xlsx', engine = 'xlsxwriter')

finaldf.to_excel(writer, sheet_name = 'Sheet1')
writer.save()


