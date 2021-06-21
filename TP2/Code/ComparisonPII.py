import scipy.io as sio
from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
import matplotlib.pyplot as plt
import numpy as np

#Get SPICE data
LTR = LTSpiceRawRead("../Spice/FlyBack_CL_realimentado_vref.raw")

t = np.abs(np.asarray(LTR.get_trace(0).data))*1e6

Vsw = np.asarray(LTR.get_trace("V(vds)").data)

Vpri = np.asarray(LTR.get_trace("V(vprim+)").data) - np.asarray(LTR.get_trace("V(vds)").data)
Ipri = np.asarray(LTR.get_trace("I(L1)").data)

Vsec = np.asarray(LTR.get_trace("V(vsec+)").data)
Isec = np.asarray(LTR.get_trace("I(L2)").data)
Vcom=np.asarray(LTR.get_trace("V(v_comp)").data)
Idio = np.asarray(LTR.get_trace("I(D1)").data)

Vo = np.asarray(LTR.get_trace("V(vout1)").data)
Vg = np.asarray(LTR.get_trace("V(vg)").data)

Icap=np.asarray(LTR.get_trace("I(C7)").data)
Vosc = np.asarray(LTR.get_trace("V(vosc)").data)
Vcap=np.asarray(LTR.get_trace("V(vcap)").data)
#TENSIÓN DE GATE Y DE SW
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
#plt.grid(which='minor')
plt.plot(t,Vg, label="Tensión de Gate")
plt.plot(t,Vsw, label="Tensión de SW")
plt.plot(t,Vosc, label="Tensión del Oscilador")
plt.legend()
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIII\ImagenesParteIII\TensionesVarias1.png')
plt.show()

#TENSIÓN SALIDA
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
#plt.grid(which='minor')
plt.plot(t,Vo)
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIII\ImagenesParteIII\ Vo.png')
plt.show()


#TENSIÓN COMP
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
#plt.grid(which='minor')
plt.plot(t,Vcom)
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIII\ImagenesParteIII\ Vcom.png')
plt.show()

#CORRIENTE DE DIODO
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Corriente [A]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
#plt.grid(which='minor')
plt.plot(t,Idio)
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIII\ImagenesParteIII\Idiodo.png')
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
ax2.plot(t, -Ipri, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIII\ImagenesParteIII\Primario.png')
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
ax2.plot(t, -Isec, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIII\ImagenesParteIII\Secundario.png')
plt.show()



#CAP SNUBBER
fig, ax1 = plt.subplots(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.grid(which='major')
plt.grid(which='minor')
color = 'tab:red'
ax1.set_xlabel("Tiempo $[\mu s]$")
ax1.set_ylabel("Tensión [V]", color=color)
ax1.plot(t, Vcap, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel("Corriente [A]", color=color)  # we already handled the x-label with ax1
ax2.plot(t, -Icap, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIII\ImagenesParteIII\Cap_snub.png')
plt.show()