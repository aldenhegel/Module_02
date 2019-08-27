import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.dates as md 
import requests
import json
import numpy as np 
from functools import reduce

# exchange rate
url = 'https://kurs.web.id/api/v1/bca'
data = requests.get(url)
data = data.json()
rate = (int(data['jual']) + int(data['beli'])) / 2

# microsoft
dfmsft = pd.read_csv(
    'MSFT.csv',
    usecols = [0, 4], 
    index_col = False,
    parse_dates = ['Date']
)
dfmsft.set_index('Date', inplace = True)
dfmsft.sort_index()

# apple
dfaapl = pd.read_csv(
    'AAPL.csv',
    usecols = [0, 4],
    index_col = False,
    parse_dates = ['Date']
)
dfaapl.set_index('Date', inplace = True)
dfaapl.sort_index()

# facebook
dffb = pd.read_csv(
    'FB.csv',
    usecols = [0, 4],
    index_col = False,
    parse_dates = ['Date']
)
dffb.set_index('Date', inplace = True)
dffb.sort_index()

# google
dfgoog = pd.read_csv(
    'GOOG.csv',
    usecols = [0, 4],
    index_col = False,
    parse_dates = ['Date']
)
dfgoog.set_index('Date', inplace = True)
dfgoog.sort_index()

# telkomsel
dftlkm = pd.read_csv(
    'telkom.csv', 
    usecols = [1, 3],
    index_col = False,
    parse_dates = ['Tanggal']
    )

dftlkm.rename(
    columns = {'Tanggal': 'Date'},
    inplace = True
)

dftlkm.set_index('Date', inplace = True)
dftlkm = dftlkm.sort_index()

# indosat
dfidst = pd.read_csv(
    'indosat.csv',
    usecols = [1, 3],
    index_col = False,
    parse_dates = ['Tanggal']
)

dfidst.rename(
    columns = {'Tanggal': 'Date'},
    inplace = True
)

dfidst.set_index('Date', inplace = True)
dfidst = dfidst.sort_index()

# fren
dffren = pd.read_csv(
    'smartfren.csv',
    usecols = [1, 3],
    index_col = False,
    parse_dates = ['Tanggal']
)

dffren.rename(
    columns = {'Tanggal': 'Date'},
    inplace = True
)

dffren.set_index('Date', inplace = True)
dffren = dffren.sort_index()

# xl
dfxl = pd.read_csv(
    'xl.csv',
    index_col = False,
    usecols = [1, 3],
    parse_dates = ['Tanggal']
)

dfxl.rename(
    columns = {'Tanggal': 'Date'},
    inplace = True
)

dfxl.set_index('Date', inplace = True)
dfxl = dfxl.sort_index()

# ==============================================================================
data_frames = [
    dftlkm, 
    dfidst,
    dffren,
    dfxl,
    dfaapl,
    dfmsft,
    dffb,
    dfgoog
    ]

# merge dataframes
df_merged = reduce(
    lambda left, right: pd.merge(
        left,
        right, 
        on = ['Date'], 
        how = 'outer'
        ), 
    data_frames
    )

df_merged.columns = ['tlkm', 'idst', 'fren', 'xl', 'aapl', 'msft', 'fb', 'goog']

# separating df's 
dftlkm['Close'] = df_merged['tlkm'].interpolate() / rate
dfidst['Close'] = df_merged['idst'] / rate
dffren['Close'] = df_merged['fren'] / rate
dfxl['Close'] = df_merged['xl'] / rate

dfaapl['Close'] = df_merged['aapl'].interpolate()
dfmsft['Close'] = df_merged['msft'].interpolate()
dffb['Close'] = df_merged['fb'].interpolate()
dfgoog['Close'] = df_merged['goog'].interpolate()

# plot
plt.style.use('seaborn')
plt.plot(
    dfaapl.index, dfaapl['Close'],
    dfmsft.index, dfmsft['Close'],
    dffb.index, dffb['Close'],
    dfgoog.index, dfgoog['Close'],
    dftlkm.index, dftlkm['Close'],
    dfidst.index, dfidst['Close'],
    dffren.index, dffren['Close'],
    dfxl.index, dfxl['Close']
)
plt.legend(
    ['Apple',
    'Microsoft',
    'Facebook',
    'Google',
    'Telkomsel',
    'Indosat',
    'Smartfren',
    'XL']
)
plt.xlabel('Date')
plt.ylabel('$ USD')
plt.xticks(rotation = 90)

# set axis
ax = plt.gca()  #get current axis
ax.xaxis.set_major_locator(md.MonthLocator(
    interval = 6
))
# date formatting
ax.xaxis.set_major_formatter(md.DateFormatter(
    '%m-%Y'
))
plt.show()