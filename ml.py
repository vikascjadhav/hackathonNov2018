
import pandas as pd 

"""
Attribute from data given for learning

[
 'date', 'stock', 'binNum', 'binStartTime', 'binEndTime','auctionIndicator',
 'volume', 'binStartPrice', 'binEndPrice','day_openPrice', 'day_closePrice', 'day_lowPrice',
 'day_highPrice', 'output_remainingVolume', 'output_closeAuctionVolume',
 'output_closePriceDirection'
 ],
"""



file_data = pd.read_pickle('trainingData1.pkl',compression="zip")

print(file_data.binNum)
""" import matplotlib.pyplot as plt
y = data.binStartTime
x = data.date
plt.scatter(x, y)
plt.show()  """

data = file_data.drop(['output_remainingVolume','output_closeAuctionVolume','output_closePriceDirection'], 1)
rvolume_labels =  file_data['output_remainingVolume']

from sklearn.preprocessing import MinMaxScaler
scalarX, scalarY = MinMaxScaler(), MinMaxScaler()

y = scalarY.fit_transform(rvolume_labels.values.reshape(-1,1))

print("Completed")
