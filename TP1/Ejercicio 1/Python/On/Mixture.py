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
IGSIO=65E-3


VTH=4
VGSO=12
VGSIO=5.5
VD0=13

IGSO=12/RG
ION= VGSO/(RL+RDS)*D
IOFF=ION

VDSON=RDS*ION
deltaQ=7.3E-9#fijate que en el spice dice otra cosa

#Constantes de tiempo

tau1=RG*Cgs_plus_cgd1
tau2=RG*Cgs_plus_cgd2

ton=-tau1*np.log(1-VTH/VGSO)#30.41E-9

tri=-tau1*np.log((VGSO-VGSIO)/(VGSO)) - ton#5.198e-08-ton
tvf=deltaQ*RG/(VGSO-VGSIO) #1.7358e-07-tri-ton

tend=9.735e-07




t1= np.linspace(0,ton,100)
t2= np.linspace(ton,tri+ton,100)
t3= np.linspace(ton+tri,tvf+tri+ton,100)
t4= np.linspace(tvf+tri+ton,tend,100)
tvf1=np.linspace(tri+ton,tvf*1+tri+ton,int(100*1))
#tvf2=np.linspace(tvf*0.5+tri+ton,tvf+tri+ton,int(100*0.5))
VGS=[]

VGS1=(VGSO*(1-np.exp(-t1/tau1)))

VGS2=(VGSO*(1-np.exp(-t2/tau1)))

VGS3= VGSIO+0*t3

delta=tvf+tri+ton
VGS4=((VGSO-VGSIO)*(1-np.exp(-(t4-delta)/tau2)))+VGSIO

off=0.76E-7
plt.figure(num=1, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.plot(t1+off,VGS1,color='c', label='Teorico')
plt.plot(t2+off,VGS2,color='r')
plt.plot(t3+off,VGS3,color='g')
plt.plot(t4+off,VGS4,color='b')




IGS=[]

IGS1=(IGSO*(np.exp(-t1/tau1)))

IGS2=(IGSO*(np.exp(-t2/tau1)))

IGS3= IGSIO+0*t3


IGS4=(IGSIO*(np.exp(-(t4-delta)/tau2)))



VDS=[]


VDS1=(VD0+0*(np.exp(-t1/tau1)))

VDS2=VDS1

VDS3=((VD0)-((VD0-VDSON)*(tvf1-(ton+tri))/(tvf)))

#VDS4=tvf2*VDSON
VDS5=t4*0+VDSON



IDS=[]

IDS1=(0*(np.exp(-t1/tau1)))

IDS2=(ION*(t2-ton)/(tri))

IDS3=ION+t3*0

IDS4=ION+t4*0


##################spice
LTR = LTSpiceRawRead("ON_commute.raw")


#LTR = LTSpiceRawRead("Off_commute.raw")


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



#plt.figure(num=1, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')

plt.ylabel("VGS")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.plot(t,Vgs,'--',color='c', label='Simulado')
plt.legend()
plt.show()

plt.figure(num=2, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("VDS")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.plot(t,Vds,'--',color='c', label='Simulado')
plt.plot(t1+off,VDS1,color='c',label='Teorico')
plt.plot(t2+off,VDS2,color='r')

plt.plot(tvf1+off,VDS3,color='g')

plt.plot(t4+off,VDS5,color='g')
plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.legend()
plt.show()

plt.figure(num=3, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("IG")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Ig,'--',color='c', label='Simulado')
plt.plot(t1+off,IGS1,color='c',label='Teorico')
plt.plot(t2+off,IGS2,color='r')
plt.plot(t3+off,IGS3,color='g')
plt.plot(t4+off,IGS4,color='b')#, label='')
plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.legend()
plt.show()

plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("IDS")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Ids,'--',color='c',label='Simulado')
plt.plot(t1+off,IDS1,color='c',label='Teorico')
plt.plot(t2+off,IDS2,color='r')
plt.plot(t3+off,IDS3,color='g')
plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.legend()
plt.show()

plt.figure(num=5, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("ID")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Id,color='c')
plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.legend()
plt.show()

plt.figure(num=6, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Il")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Il,color='c')
plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.legend()
plt.show()

