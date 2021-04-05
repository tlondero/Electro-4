from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
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
off=5.8e-7


VTH=4
VGSO=12
VDSO=13.3
VGSIO=5.5

IGSO=12/RG
ION= VGSO/(RL+RDS)*D
IOFF=ION
IGSIO=55E-3

VDSON=RDS*ION
deltaQ=7.3E-9#fijate que en el spice dice otra cosa

#Constantes de tiempo

tau1=RG*Cgs_plus_cgd1
tau2=RG*Cgs_plus_cgd2

toff=-tau2*np.log(VGSIO/VGSO)


trv=deltaQ*RG/(VGSIO) #

tfi=-tau1*np.log((VTH)/(VGSIO)) #

tend=9.7358e-07



t0=np.linspace(0,off,100)
t1= np.linspace(0,toff,100)
t2= np.linspace(toff,toff+trv,100)
t3= np.linspace(toff+trv,toff+trv+tfi,100)
t4= np.linspace(toff+trv+tfi,tend,100)

VGS=[]
VGS0=VGSO+t0*0
VGS1=(VGSO*(np.exp(-t1/tau2)))

VGS2=VGSIO+0*t2

delta=trv+toff


VGS3= (VGSIO*(np.exp(-(t3-delta)/tau1)))


VGS4=(VGSIO*(np.exp(-(t4-delta)/tau1)))



plt.figure(num=1, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.plot(t0,VGS0,color='g')
plt.plot(t1+off,VGS1,color='g')
plt.plot(t2+off,VGS2,color='g')
plt.plot(t3+off,VGS3,color='g')
plt.plot(t4+off,VGS4,color='g',label='Teórico')



IGS=[]
IGS0=0+t0*0
IGS1=-(IGSO*(np.exp(-t1/tau2)))

IGS2=-IGSIO+0*t2

IGS3= -(IGSIO*(np.exp(-(t3-delta)/tau1)))

IGS4=-(IGSIO*(np.exp(-(t4-delta)/tau1)))

VDS=[]

VDS0=VDSON+0*t0
VDS1=(VDSON+0*(np.exp(-t1/tau1)))

VDS2=(((VDSO-VDSON)*(t2-(toff))/(trv)))+VDSON

VDS3=VDSO+t3*0

VDS5=t4*0+VDSO



IDS=[]
IDS0=ION+t0*0
IDS1=ION+t1*0

IDS2=ION+t2*0

IDS3=(ION*(1-(t3-toff-trv)/(tfi)))

IDS4=t4*0


##################spice

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



#plt.figure(num=1, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')

plt.ylabel("VGS")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Vgs,'--',color='c',label='Simulado')
plt.legend()
plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.show()

plt.figure(num=2, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("VDS")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Vds,'--',color='c',label='Simulado')
plt.plot(t0,VDS0,color='g',label='Teórico')
plt.plot(t1+off,VDS1,color='g')
plt.plot(t2+off,VDS2,color='g')

plt.plot(t3+off,VDS3,color='g')

plt.plot(t4+off,VDS5,color='g')
plt.legend()
plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.show()

plt.figure(num=3, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("IG")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Ig,'--',color='c',label='Simulado')
plt.plot(t0,IGS0,color='g',label='Teórico')
plt.plot(t1+off,IGS1,color='g')
plt.plot(t2+off,IGS2,color='g')
plt.plot(t3+off,IGS3,color='g')
plt.plot(t4+off,IGS4,color='g')#, label='')
plt.legend()
plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.show()

plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("IDS")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Ids,'--',color='c',label='Simulado')
plt.plot(t0,IDS0,color='g',label='Teórico')
plt.plot(t1+off,IDS1,color='g')
plt.plot(t2+off,IDS2,color='g')
plt.plot(t3+off,IDS3,color='g')
plt.plot(t4+off,IDS4,color='g')
plt.legend()
plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.show()

plt.figure(num=5, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("ID")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Id,color='c')
plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.show()

plt.figure(num=6, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Il")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t,Il,color='c')
plt.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.show()

