import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##importing data - csv file into Pandas dataframe (milestone 2)
data=pd.read_csv("BitCoin.csv") ##data source https://www.kaggle.com/aditeloo/bitcoin

##to show the csv file imported is using Pandas Dataframe
print(type(data))

##sorting the data in ascending order of bitcoin market price (milestone 3)
data.sort_values("btc_market_price")

##script to show the dataframe information (number of columns, type, name etc)
print(data.info())

print("===============================")

##identifying the total missing values in dataframe (milestone 3)
missingdata=data.isnull().sum()

print(missingdata) ## this returned the total of all TRUE (NULL values) in each column

print("===============================")

##Replacing missing(null) values (milestone 3)
clean_data=data.fillna(0) ##fillna is fill not available

##identifying the total missing values in dataframe (milestone 3)
missingdata=clean_data.isnull().sum()

print(missingdata) ## this returned the total of all TRUE (NULL values) in each column
print(clean_data.info()) ##non null values for all columns are 2906 now
print("===============================")

##Visualize using Matplotlib (milestone 5)
x=data.Date
y=data.btc_market_price
plt.plot(x,y)
plt.show()

bitqty=data.btc_total_bitcoins
plt.bar(x,bitqty)
plt.show()

