import scipy.io as sio
from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
import matplotlib.pyplot as plt
import numpy as np

def getData(path):
    data = sio.loadmat(path)
    dataxd = np.asarray(data['d'])
    data = []
    time = []

    timeInit = 8e-3
    for i in range(len(dataxd)):
        data.append(dataxd[i][1])
        time.append(dataxd[i][0] - timeInit)

    return np.asarray(time), np.asarray(data)

#Get SPICE data
LTR = LTSpiceRawRead("Draft4.raw")

t_s = np.abs(np.asarray(LTR.get_trace(0).data))*1e6
Vo_s = np.asarray(LTR.get_trace("Id(M1)").data)

plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$I_{D} \ [V]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t_s,Vo_s,color='b', label="$I_{D}$")
plt.legend()
plt.xlim(0, 18)
plt.savefig('..\Tex\Ejercicio-4\ImagenesEjercicio-4\ id.png')
plt.show()