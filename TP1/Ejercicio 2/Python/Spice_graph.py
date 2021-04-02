from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
import matplotlib.pyplot as plt
import numpy as np

LTR = LTSpiceRawRead("../Spice/Draft3.raw")

time = LTR.get_trace(0)
t = np.abs(np.asarray(time.data))*1e6

IL_trace = LTR.get_trace("I(L1)")
VL_trace1 = LTR.get_trace("V(vl+)")
VL_trace2 = LTR.get_trace("V(vl-)")
ID_trace = LTR.get_trace("I(D1)")
Vout_trace = LTR.get_trace("V(vout)")
Vtrig_trace = LTR.get_trace("V(vtrig)")

IL = np.asarray(IL_trace.data)*1000
VL = np.asarray(VL_trace1.data) - np.asarray(VL_trace2.data)
ID = np.asarray(ID_trace.data)
Vout = np.asarray(Vout_trace.data)
Vtrig = np.asarray(Vtrig_trace.data)

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