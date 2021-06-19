import scipy.io as sio
from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
import matplotlib.pyplot as plt
import numpy as np

#Get SPICE data
LTR = LTSpiceRawRead("../Spice/Flyback.raw")

t = np.abs(np.asarray(LTR.get_trace(0).data))*1e6

Vsw = np.asarray(LTR.get_trace("V(vs+)").data) - np.asarray(LTR.get_trace("V(vs-)").data)

Vpri = np.asarray(LTR.get_trace("V(vs-)").data)
Ipri = np.asarray(LTR.get_trace("I(L1)").data)

Vsec = np.asarray(LTR.get_trace("V(vn2+)").data)
Isec = np.asarray(LTR.get_trace("I(L2)").data)

Idio = np.asarray(LTR.get_trace("I(D1)").data)

Vo = np.asarray(LTR.get_trace("V(vout1)").data)
Vg = np.asarray(LTR.get_trace("V(vg)").data)

#TENSIÓN DE GATE Y DE SW
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Vg, label="Tensión de Gate")
plt.plot(t,Vsw, label="Tensión de SW")
plt.legend()
plt.xlim(0, 100)
plt.savefig('..\Tex\ParteII\ImagenesParteII\TensionesVarias1.png')
plt.show()

#TENSIÓN SALIDA
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Vo, label="Tensión de Salida")
plt.legend()
plt.xlim(0, 100)
plt.savefig('..\Tex\ParteII\ImagenesParteII\ Vo.png')
plt.show()

#CORRIENTE DE DIODO
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Idio, label="Corriente de Diodo")
plt.legend()
plt.xlim(0, 100)
plt.savefig('..\Tex\ParteII\ImagenesParteII\Idiodo.png')
plt.show()

#PRIMARIO
fig, ax1 = plt.subplots(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.grid(which='major')
plt.grid(which='minor')
color = 'tab:red'
ax1.set_xlabel("Tiempo $[\mu s]$")
ax1.set_ylabel("Tensión [V]", color=color)
ax1.plot(t, Vpri, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel("Corriente [A]", color=color)  # we already handled the x-label with ax1
ax2.plot(t, Ipri, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.xlim(0, 100)
plt.savefig('..\Tex\ParteII\ImagenesParteII\Primario.png')
plt.show()

#SECUNDARIO
fig, ax1 = plt.subplots(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.grid(which='major')
plt.grid(which='minor')
color = 'tab:red'
ax1.set_xlabel("Tiempo $[\mu s]$")
ax1.set_ylabel("Tensión [V]", color=color)
ax1.plot(t, Vsec, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel("Corriente [A]", color=color)  # we already handled the x-label with ax1
ax2.plot(t, Isec, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.xlim(0, 100)
plt.savefig('..\Tex\ParteII\ImagenesParteII\Secundario.png')
plt.show()