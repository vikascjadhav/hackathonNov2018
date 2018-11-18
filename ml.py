import pandas as pd 

data = pd.read_pickle('trainingData1.pkl',compression="zip")
print(data.head())
print(data.columns)
values =data.output_closeAuctionVolume
""" 
['date', 'stock', 'binNum', 'binStartTime', 'binEndTime',
       'auctionIndicator', 'volume', 'binStartPrice', 'binEndPrice',
       'day_openPrice', 'day_closePrice', 'day_lowPrice', 'day_highPrice',
       'output_remainingVolume', 'output_closeAuctionVolume',
       'output_closePriceDirection'],
        """

print(values.head())

import matplotlib.pyplot as plt
y = data.binStartTime
x = data.date
plt.scatter(x, y)
plt.show()  # or plt.savefig("name.png")