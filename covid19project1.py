
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt


table = pd.read_csv("pb_covid_data.csv")
# print(table)

X = table.confirmed.values
Y = table.date.values

# print(X)
# print(Y)

# plt.scatter(X, Y)
# plt.show()
#
# reshaping into 2d ARRAY
X = X.reshape(len(X), 1)

Y = Y.reshape(len(Y), 1)
# print(X)
# print(Y)
# model=LinearRegression()
# model.fit(X,Y)