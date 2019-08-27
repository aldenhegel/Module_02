import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('indo_12_1.xls', skiprows=3, skipfooter=2, na_values='-')
df.rename(columns={'Unnamed: 0': 'Province'}, inplace=True)

# data for indonesia
ind = df.tail(1)
indx = list(ind.columns)[1:]
indy = list(ind.values[0])[1:]
legi = list(ind['Province'])[0]

# removing 'INDONESIA'
df.drop(ind.index, inplace=True)

# null handling 
df = df.dropna(subset = [1971, 2000])

# province with min population in 1971
minimum = df[df[1971] == df[1971].min()]
minx = list(minimum.columns)[1:]
miny = list(minimum.values[0])[1:]
legmin = list(minimum['Province'])[0]

# province with max population in 2000
maximum = df[df[2000] == df[2000].max()]
maxx = list(maximum.columns)[1:]
maxy = list(maximum.values[0])[1:]
legmax = list(maximum['Province'])[0]

# plot
plt.style.use('seaborn')
plt.plot(indx, indy, 'b-',
        minx, miny, 'r-',
        maxx, maxy, 'g-')
plt.legend([legi, legmin, legmax])
plt.grid(True)
plt.show()