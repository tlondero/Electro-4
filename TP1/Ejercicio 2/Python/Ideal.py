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

#Get MATLAB data
t_m, Vo_m = getData('../Matlab/ideal_duty_vo.mat')
t_m = np.asarray(t_m)*1e6

#Get SPICE data
LTR = LTSpiceRawRead("../Spice/Draft3_ideal.raw")

t_s = np.abs(np.asarray(LTR.get_trace(0).data))*1e6
Vo_s = np.asarray(LTR.get_trace("V(vout)").data)

plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$V_{Out} \ [V]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t_m,Vo_m,color='r', label="Simulink")
plt.plot(t_s,Vo_s,color='b', label="LTSpice")
plt.legend()
plt.xlim(0, 50)
plt.savefig('..\..\Tex\Ejercicio-2\ImagenesEjercicio-2\ vout.png')
plt.show()