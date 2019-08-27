import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates

df = pd.read_csv(
    'telkom.csv', 
    index_col = False,
    parse_dates = ['Tanggal']
    )

df.set_index('Tanggal', inplace = True)
df = df.sort_index()

# print(df['Close'].max())
# print(df[df['Open'] == df['Close'].max()])

# by range
# print(df['2016-01-10':'2017-01-10'])

# print(df['2019-03']['Close'].mean())
# print(df['2019-03']['Close'].max())
# print(df['2019-03']['Close'].min())

# ==============================================================================

# plt.style.use('seaborn')

# plt.plot(
#     df.index,
#     df['Close'],
#     'r-'
# )
# plt.subplots_adjust(bottom = .21)
# plt.xlabel('Tanggal')
# plt.ylabel('Rp')
# plt.xticks(rotation = 60)
# plt.grid(True)

# # set axis
# ax = plt.gca()  #get current axis
# ax.xaxis.set_major_locator(mdates.MonthLocator(
#     interval = 3
# ))
# # date formatting
# ax.xaxis.set_major_formatter(mdates.DateFormatter(
#     '%m-%Y'
# ))

# plt.show()

# ==============================================================================
# resample MonthEnd, WeekEnd, Quarter, Yearly
print(df['2019-02':'2019-05']['Close'].resample('Q').mean())