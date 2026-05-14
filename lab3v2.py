import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
copper_data = sm.datasets.copper.load_pandas().data
copper_data.index = pd.date_range('1951-01-01', '1975-01-01', freq='YS')
data_61_75 = copper_data.loc['1961':'1975']
dates = data_61_75.index
cuprice = data_61_75.COPPERPRICE
alprice = data_61_75.ALUMPRICE
plt.plot(dates, cuprice, label="Copper price")
plt.plot(dates, alprice, label="Aluminium price")
plt.legend(frameon=True, facecolor='lightgray', edgecolor='none')
plt.show()