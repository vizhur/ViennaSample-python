import pickle
import sys
import pandas as pd
import numpy as np
import os

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import cross_validation

from azureml.sdk import data_collector

# create the outputs folder
os.makedirs('./outputs', exist_ok=True)

# Initialize the logger
run_logger = data_collector.current_run() 

# load data
data = pd.read_csv('mydata.csv', delimiter=',', na_values="n/a")
print ('Dataset shape: {}'.format(data.shape))

# split
train, test = sklearn.cross_validation.train_test_split(data, train_size=0.7, random_state=123)

# load features and labels, assuming the last col is the label col.
X_train = train.iloc[:, :-1]
Y_train = train.iloc[:, -1]
X_test = test.iloc[:, :-1]
Y_test = test.iloc[:, -1]

# train the model
model = sklearn.linear_model.LinearRegression()
model.fit(X_train, Y_train)

# evaluate the model
Y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test, Y_pred)
print('Mean Squared Error: {}.'.format(mse))

# log MSE
run_logger.log("Mean Squared Error", mse)

# serialize the model on disk in the special 'outputs' folder
f = open('./outputs/model.pkl', 'wb')
pickle.dump(model, f)
f.close()
