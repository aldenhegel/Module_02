import csv
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import axes3d
import numpy as np 

# extract data
with open('Persentase Perokok RI.csv', 'r') as stats:
    reader = csv.DictReader(stats)
    province = []
    cig1 = []
    cig2 = []
    for item in reader:
        province.append(item['Provinsi'])
        cig1.append(float(item['2015']))
        cig2.append(float(item['2016']))


fig = plt.figure('Persentase Perokok RI')
ax = plt.subplot(111, projection='3d')

# x axis
x1 = np.zeros(len(province))
x2 = np.repeat(1, len(province))
dx = np.repeat(0.5, len(province))

# y oordinate
y1 = np.arange(len(province))
y2 = y1
dy = dx

# z coordinate
z1 = x1
z2 = x1
dz1 = cig1
dz2 = cig2

# scattered province names
xsctr = np.arange(0.5, 1, 0.5 / 34)
ysctr = y1
zsctr = np.arange(30, 0, -30 / 34)

# bar projection
ax.bar3d(x1, y1, z1, dx, dy, dz1, color = '#003f5c', alpha = 0.8)
ax.bar3d(x2, y2, z2, dx, dy, dz2, color = '#ffa600', alpha = 0.8)  

# province projection
for item, count in zip(province, range(len(province))):   
    ax.scatter(xsctr[count], ysctr[count], zsctr[count], marker = f'${item}$', s = 300)

# axis naming
ax.set_xlabel('Year')
ax.set_zlabel('% Percentage')

# xticks rename
plt.xticks([0.25, 1.25], [2015, 2016])

# yticks rename
plt.yticks(y1, province)
plt.yticks(rotation = 90)


plt.show()














# counter = 0
# y = []
# for item in province:
#     counter += 1 
#     y.append(counter)

# dy = []
# for item in province:
#     dy.append(0.5)

# x = np.ones(34)
# y = np.array(y)
# z = np.zeros(34)   #must be 2 dimensional
# dx = np.ones(34)
# dy = np.array(dy)
# dz = x1


# ax.bar3d(x, y, z, dx, dy, dz)  

# ax.set_xlabel('Year')
# ax.set_ylabel('Province')
# ax.set_zlabel('% Percentage')
# plt.show()