import scipy.io as sio
#import h5py
import matplotlib.pyplot as plt
import numpy as np


def getData(path):

    data = sio.loadmat(path)
    dataxd = np.asarray(data['d'])
    data = []
    time = []
    for i in range(len(dataxd)):
        data.append(dataxd[i][1])
        time.append(dataxd[i][0])

    return time, data

t, VL = getData('../Matlab/vl.mat')
t, IL = getData('../Matlab/il.mat')
t, ID = getData('../Matlab/id.mat')
t, Vout = getData('../Matlab/vo.mat')
t, Vtrig = getData('../Matlab/vtrig.mat')

plt.figure(num=1, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$I_L \ [mA]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,IL,color='c')
plt.show()

plt.figure(num=2, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$V_L \ [V]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,VL,color='c')
plt.show()

plt.figure(num=3, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$I_D \ [A]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,ID,color='c')
plt.show()

plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$V_{Out} \ [V]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Vout,color='c')
plt.show()

plt.figure(num=5, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$V_{Trig} \ [V]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Vtrig,color='c')
plt.show()

fig, ax1 = plt.subplots(num=5, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')

color = 'tab:red'
ax1.set_xlabel('Tiempo $[\mu s]$')
ax1.set_ylabel('$V_L \ [V]$', color=color)
ax1.plot(t, VL, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('$I_L \ [mA]$', color=color)  # we already handled the x-label with ax1
ax2.plot(t, IL, color=color)
ax2.tick_params(axis='y', labelcolor=color)
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

plt.figure(num=1, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$I \ [mA]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,IL,color='c', label="$I_L$")
plt.plot(t,ID*1000,color='b', label="$I_D$")
plt.legend()
plt.show()