import scipy.io as sio
from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
import matplotlib.pyplot as plt
import numpy as np

#Get SPICE data
LTR = LTSpiceRawRead("../Spice/FlyBack_CL_realimentado_vref.raw")

t = np.abs(np.asarray(LTR.get_trace(0).data))*1e6

Vo = np.asarray(LTR.get_trace("V(vout1)").data)


#TENSIÓN SALIDA
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
#plt.grid(which='minor')
plt.plot(t,Vo)
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIII\ImagenesParteIII\Vout_esr.png')
plt.show()
