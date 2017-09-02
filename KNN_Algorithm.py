import quandl
import numpy as np
import scipy
import matplotlib.pyplot as plt
import xlsxwriter
import pandas as pd
import xlrd
import sklearn
from sklearn import preprocessing, cross_validation, neighbors


xl = pd.ExcelFile("30 Days_Data File_Run_MOD.xlsx")
xl.sheet_names

df = xl.parse("Sheet1")

IPCRatio = df['Index P/C Ratio'].tolist()
PCRatio = df['P/C Ratio'].tolist()
#Close = df['Close'].tolist()

TDV = df['30 Day Variance'].tolist()
Skew = df['30 Day CBOE Skew'].tolist()

Result_Daily = df['Up/Down'].tolist()

df.fillna(-99999, inplace=True)

X = np.array(df.drop(['Up/Down'], 1))
Y = np.array(df['Up/Down'])

X = preprocessing.scale(X)

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)

#print(len(X), len(Y))

print(accuracy)


