from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
import scipy.signal
import matplotlib.pyplot as plt
import numpy as np


import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import math
#componentes
RG=100
L=220E-6
RL=1
RDS=0.16
fsw=60E3
tauRL=L/RL
D=0.5
Cgs_plus_cgd1=750E-12
Cgs_plus_cgd2=1150E-12



VTH=4
VGSO=12

VGSIO=5.5
VD0=12
VDL=6.47
IGSO=12/RG
ION= 5.17
IOFF=ION

VDSON=RDS*ION
deltaQ=7.3E-9#fijate que en el spice dice otra cosa

#Constantes de tiempo

tau1=RG*Cgs_plus_cgd1
tau2=RG*Cgs_plus_cgd2

t1= np.linspace(0,1/(2*60E3),100)
t2= np.linspace(1/(2*60E3),1/60E3,100)

off=0.74E-7+2.97E-7
Il1= (-t1*VDL/L) +ION + (abs(min((-t1*VDL/L)))+abs(max((-t1*VDL/L))))/2
Il2= ((t2)*VDL/L) +ION -(abs(min((-t2*VDL/L)))+abs(max((-t2*VDL/L))))/2


##################spice
LTR = LTSpiceRawRead("currs.raw")


time = LTR.get_trace(0)
t = np.abs(np.asarray(time.data))

Id_trace = LTR.get_trace("I(D1)")
Il_trace = LTR.get_trace("I(L1)")


Id=np.asarray(Id_trace.data)
Il=np.asarray(Il_trace.data)




plt.figure(num=2, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("IL")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
#plt.plot(t,Il,'--',color='c2',label='Simulado')
plt.plot(t1+off,Il1,color='c')
plt.plot(t2+off,Il2,color='r')
plt.legend()
plt.ticklabel_format(axis='x', style='sci', scilimits=(2,-2))
plt.ylim(5.17-1,5.17+1)
plt.show()




plt.figure(num=2, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("ID")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
#plt.plot(t,Id,'--',color='c',label='Simulado')
plt.plot(t1+off,Il1,color='c',label='Teorico')
plt.plot(t2+off,0*Il2,color='r')
plt.legend()
plt.ticklabel_format(axis='x', style='sci', scilimits=(2,-2))
plt.ylim(-0.3,5.75)
plt.show()
