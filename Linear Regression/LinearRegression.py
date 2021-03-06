### Linear Regression Model on CalCOFI Kaggle dat to predict Temperature using Sanity of the water

### Data is collected from 1949 to 2017 and contains more than 150,000 samples
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## importing data from csv file"""

dataset = pd.read_csv('bottle.csv')
Data=dataset[['Salnty', 'T_degC']]

"""## Plotting the data salnty vs T_degC"""

from matplotlib import pyplot as plt
import seaborn as sns
plt.figure(figsize=(13, 9))
plt.scatter(Data["Salnty"], Data["T_degC"],s=65)
plt.xlabel('Slnty',fontsize=25)
plt.ylabel('Temp',fontsize=25)
plt.title('slnty-Temp',fontsize=25)
plt.show()

"""### Here I'm taking all the values to build the models. On the internet you may see models that used around 500 data points and gets high r2 score. But I'll show why linear regression is not suited for this data. So we will take all samples and split them in to train and tests."""

Data.columns = ['Sal', 'Temp']
print(Data.head(10))

"""### Filling NAN/missing values"""

Data.fillna(method='ffill', inplace=True)

"""## creating X and Y variable"""

X = pd.DataFrame(np.c_[Data['Sal']], columns = ['Sal'])
Y = Data['Temp']

"""## Splitting data in to test and train sets"""

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=5)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

"""## Training Linear regression model with training data"""

from sklearn.linear_model import LinearRegression 
regressor = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)
regressor.fit(X_train, Y_train)

"""## Predicting for test sets"""

y_pred = regressor.predict(X_test)

"""## Calculating R2 score using r2_score methode from sklearn library"""

from sklearn.metrics import r2_score

r2 = r2_score(Y_test, y_pred)
print(r2)

"""## Plotting data and Linear regression line to undersatand the reason for low r2 score. I have also trained model with 500 data samples where my r2 score was 0.84 due to less data."""

from matplotlib import pyplot as plt
import seaborn as sns
plt.scatter(X_train, Y_train,s=65)
plt.plot(X_train,regressor.predict(X_train), color = 'red')
plt.xlabel('Slnty',fontsize=25)
plt.ylabel('Temp',fontsize=25)
plt.title('slnty-Temp',fontsize=25)
plt.show()
