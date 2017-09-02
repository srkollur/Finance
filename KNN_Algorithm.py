import quandl
import numpy as np
import scipy
import matplotlib.pyplot as plt
import xlsxwriter
import pandas as pd
import xlrd
import sklearn
from sklearn import preprocessing, cross_validation, neighbors


#Data file is read in next line

xl = pd.ExcelFile("30 Days_Data File_Run.xlsx")
xl.sheet_names

df = xl.parse("Sheet1")

Result_Daily = df['Up/Down'].tolist()

df.fillna(-99999, inplace=True)

X = np.array(df.drop(['Up/Down'], 1))

#X is the data used to predict

Y = np.array(df['Up/Down'])

#Y is the prediction

X = preprocessing.scale(X)

#test size can be modified, 0.2 means 80% of data used to train, 20% used to test

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)

#print(len(X), len(Y))

print(accuracy)


