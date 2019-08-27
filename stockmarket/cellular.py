import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.dates as md 

# indosat
dfidst = pd.read_csv(
    'indosat.csv',
    index_col = False,
    parse_dates = ['Tanggal']
)
dfidst.set_index('Tanggal', inplace = True)
dfidst = dfidst.sort_index()

# fren
dffren = pd.read_csv(
    'smartfren.csv',
    index_col = False,
    parse_dates = ['Tanggal']
)
dffren.set_index('Tanggal', inplace = True)
dffren = dffren.sort_index()

# telkom
dftlkm = pd.read_csv(
    'telkom.csv',
    index_col = False,
    parse_dates = ['Tanggal']
)
dftlkm.set_index('Tanggal', inplace = True)
dftlkm = dftlkm.sort_index()

# xl
dfxl = pd.read_csv(
    'xl.csv',
    index_col = False,
    parse_dates = ['Tanggal']
)
dfxl.set_index('Tanggal', inplace = True)
dfxl = dfxl.sort_index()


# plot
plt.style.use('seaborn')
plt.plot(
    dftlkm.index, dftlkm['Close'], 'r-',
    dfidst.index, dfidst['Close'], 'y-',
    dfxl.index, dfxl['Close'], 'b-',
    dffren.index, dffren['Close'], 'k-'
    )

# set axis
ax = plt.gca()
ax.xaxis.set_major_locator(md.MonthLocator(
    interval=3
))
ax.xaxis.set_major_formatter(md.DateFormatter(
    '%b %y'
))

plt.title('Cellular Data Provider Stocks')
plt.legend(['Telkomsel', 'Indosat', 'XL', 'SmartFren'])
plt.xlabel('Month')
plt.ylabel('Rp')
plt.xticks(rotation = 90)
plt.show()