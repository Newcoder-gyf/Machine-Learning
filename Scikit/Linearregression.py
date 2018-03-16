import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("ccpp.csv")

#print(data.head())

#print(data.shape)

X = data[['AT', 'V', 'AP', 'RH']]
#print (X.head())

y = data[['PE']]
#print(y.head())

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

print (X_train.shape)
print (y_train.shape)
print (X_test.shape)
print (y_test.shape)

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train, y_train)

print (linreg.intercept_)
print (linreg.coef_)


y_pred = linreg.predict(X_test)
from sklearn import metrics
print ("MSE:",metrics.mean_squared_error(y_test, y_pred))
print ("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print("\nnew X \n")

X = data[['AT', 'V', 'AP']]
y = data[['PE']]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train, y_train)

y_pred = linreg.predict(X_test)
from sklearn import metrics

print ("MSE:",metrics.mean_squared_error(y_test, y_pred))

print ("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print("\nnew X \n")

X = data[['AT', 'V', 'AP', 'RH']]
y = data[['PE']]
from sklearn.model_selection import cross_val_predict
predicted = cross_val_predict(linreg, X, y, cv=10)

print ("MSE:",metrics.mean_squared_error(y, predicted))

print ("RMSE:",np.sqrt(metrics.mean_squared_error(y, predicted)))

print("plot\n")

fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()