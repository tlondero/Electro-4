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
t_m, VL_m = getData('../Matlab/vl.mat')
t_m, IL_m = getData('../Matlab/il.mat')
t_m, ID_m = getData('../Matlab/id.mat')
t_m, Vout_m = getData('../Matlab/vo.mat')
t_m, Vtrig_m = getData('../Matlab/vtrig.mat')
t_m = np.asarray(t_m)*1e6

# t_m_ideal, Vo_ideal = getData('../Matlab/ideal_vo.mat')
# t_m_ideal = np.asarray(t_m_ideal)*1e6

#Get SPICE data
LTR = LTSpiceRawRead("../Spice/Draft3.raw")

time = LTR.get_trace(0)
t_s = np.abs(np.asarray(time.data))*1e6

IL_trace = LTR.get_trace("I(L1)")
VL_trace1 = LTR.get_trace("V(vl+)")
VL_trace2 = LTR.get_trace("V(vl-)")
ID_trace = LTR.get_trace("I(D1)")
Vout_trace = LTR.get_trace("V(vout)")
Vtrig_trace = LTR.get_trace("V(vtrig)")

IL_s = np.asarray(IL_trace.data)
VL_s = np.asarray(VL_trace1.data) - np.asarray(VL_trace2.data)
ID_s = np.asarray(ID_trace.data)
Vout_s = np.asarray(Vout_trace.data)
Vtrig_s = np.asarray(Vtrig_trace.data)

plt.figure(num=1, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$I_L \ [mA]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t_m,IL_m*1e3,color='r', label="Simulink")
plt.plot(t_s,IL_s*1e3,color='b', label="LTSpice")
plt.legend()
plt.xlim(0, 50)
plt.ylim(200, 800)
plt.savefig('..\..\Tex\Ejercicio-2\ImagenesEjercicio-2\il.png')
plt.show()

plt.figure(num=2, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$V_L \ [V]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t_m,VL_m,color='r', label="Simulink")
plt.plot(t_s,VL_s,color='b', label="LTSpice")
plt.legend()
plt.xlim(0, 50)
plt.savefig('..\..\Tex\Ejercicio-2\ImagenesEjercicio-2\ vl.png')
plt.show()

plt.figure(num=3, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$I_D \ [mA]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t_m,ID_m*1e3,color='r', label="Simulink")
plt.plot(t_s,ID_s*1e3,color='b', label="LTSpice")
plt.legend()
plt.xlim(0, 50)
plt.ylim(-1000, 1000)
plt.savefig('..\..\Tex\Ejercicio-2\ImagenesEjercicio-2\id.png')
plt.show()

plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$V_{Out} \ [V]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t_m,Vout_m,color='r', label="Simulink")
plt.plot(t_s,Vout_s,color='b', label="LTSpice")
plt.legend()
plt.xlim(0, 50)
plt.savefig('..\..\Tex\Ejercicio-2\ImagenesEjercicio-2\ vout.png')
plt.show()

plt.figure(num=5, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$V_{Trig} \ [V]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t_m,Vtrig_m,color='r', label="Simulink")
plt.plot(t_s,Vtrig_s,color='b', label="LTSpice")
plt.legend()
plt.xlim(0, 50)
plt.savefig('..\..\Tex\Ejercicio-2\ImagenesEjercicio-2\ vtrig.png')
plt.show()

# plt.figure(num=5, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
# plt.ylabel("$V_{Trig} \ [V]$")
# plt.xlabel("Tiempo $[\mu s]$")
# plt.minorticks_on()
# plt.grid(which='major')
# plt.grid(which='minor')
# plt.plot(t_m_ideal,Vo_ideal,color='r', label="Diodo ideal")
# plt.plot(t_s,Vout_s,color='b', label="Diodo real")
# plt.legend()
# plt.xlim(0, 50)
# plt.savefig('..\..\Tex\Ejercicio-2\ImagenesEjercicio-2\ vo_diodo_ideal.png')
# plt.show()