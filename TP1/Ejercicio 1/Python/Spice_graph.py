from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
import scipy.signal
import matplotlib.pyplot as plt
import numpy as np


#LTR = LTSpiceRawRead("ON_commute.raw")


LTR = LTSpiceRawRead("Off_commute.raw")


time = LTR.get_trace(0)
t = np.abs(np.asarray(time.data))

Vds_trace = LTR.get_trace("V(vd)")
Vgs_trace = LTR.get_trace("V(vg)")
Ids_trace = LTR.get_trace("Id(M1)")
Ig_trace = LTR.get_trace("Ig(M1)")
IDiode_trace = LTR.get_trace("I(D1)")
Il_trace = LTR.get_trace("I(L1)")

Vds=np.asarray(Vds_trace.data)
Vgs=np.asarray(Vgs_trace.data)
Ids=np.asarray(Ids_trace.data)
Ig=np.asarray(Ig_trace.data)
Id=np.asarray(IDiode_trace.data)
Il=np.asarray(Il_trace.data)



plt.figure(num=1, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("VDS")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Vds,color='c')
plt.show()

plt.figure(num=2, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("VGS")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Vgs,color='c')
plt.show()

plt.figure(num=3, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("IG")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Ig,color='c')
plt.show()

plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("IDS")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Ids,color='c')
plt.show()

plt.figure(num=5, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("ID")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Id,color='c')
plt.show()

plt.figure(num=6, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Il")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Il,color='c')
plt.show()

