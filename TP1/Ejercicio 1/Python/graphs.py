import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import math
#componentes
RG=100
L=220E-6
RL=1
fsw=60E3
tauRL=L/RL
D=0.5
Cgs_plus_cgd1=750E-12
Cgs_plus_cgd2=1150E-12

VTH=4
VGSO=12
VGSIO=6#mirar
VD0=12
VDSON=0
deltaQ=7.3E-9#fijate que en el spice dice otra cosa
#Constantes de tiempo

tau1=RG*Cgs_plus_cgd1
tau2=RG*Cgs_plus_cgd2

ton=-tau1*np.log(1-VTH/VGSO)#30.41E-9

tri=-tau1*np.log((VGSO-VGSIO)/(VGSO)) - ton#5.198e-08-ton
tvf=deltaQ*RG/(VGSO-VGSIO) #1.7358e-07-tri-ton

tend=5.7358e-07
ION=VGSO


IGSO=12/RG
ION= (VGSO/RL)*((1-np.exp(-(D/fsw)/tauRL))/(np.exp(((1-D)/fsw)/tauRL)-np.exp(-(D/fsw)/tauRL)))
IOFF=(VGSO/RL)*((1-np.exp(-(D/fsw)/tauRL))*np.exp(((1-D)/fsw)/tauRL)/(np.exp(((1-D)/fsw)/tauRL)-np.exp(-(D/fsw)/tauRL)))

t1= np.linspace(0,ton,100)
t2= np.linspace(ton,tri+ton,100)
t3= np.linspace(ton+tri,tvf+tri+ton,100)
t4= np.linspace(tvf+tri+ton,tend,100)
tvf1=np.linspace(tri+ton,tvf*0.2+tri+ton,int(100*0.2))
tvf2=np.linspace(tvf*0.2+tri+ton,tvf+tri+ton,int(100*0.8))

VGS=[]

VGS1=(VGSO*(1-np.exp(-t1/tau1)))

VGS2=(VGSO*(1-np.exp(-t2/tau1)))

VGS3= 6+0*t3

delta=1.7358e-07
VGS4=(6*(1-np.exp(-(t4-delta)/tau2)))+6


plt.figure(num=1, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.plot(t1,VGS1,color='c')
plt.plot(t2,VGS2,color='r')
plt.plot(t3,VGS3,color='g')
plt.plot(t4,VGS4,color='b')#, label='')

plt.ylabel("VGS")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.show()

IGS=[]

IGS1=(IGSO*(np.exp(-t1/tau1)))

IGS2=(IGSO*(np.exp(-t2/tau1)))

IGS3= 60e-3+0*t3

delta=1.7358e-07
IGS4=(60e-3*(np.exp(-(t4-delta)/tau2)))

plt.figure(num=2, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.plot(t1,IGS1,color='c')
plt.plot(t2,IGS2,color='r')
plt.plot(t3,IGS3,color='g')
plt.plot(t4,IGS4,color='b')#, label='')

plt.ylabel("IGS ")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.show()


IGS=[]

IDS1=(0*(np.exp(-t1/tau1)))

IGS2=(ION*(t2-ton)/(5.198e-08-30.41E-9))

IGS3=ION+t3*0

IGS4=ION+t4*0

plt.figure(num=3, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.plot(t1,IGS1,color='c')
plt.plot(t2,IGS2,color='r')
plt.plot(t3,IGS3,color='g')

plt.ylabel("IDS ")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.show()

VDS=[]


VDS1=(VD0+0*(np.exp(-t1/tau1)))

VDS2=VDS1

VDS3=(VD0-(VD0*(tvf1-(ton+tri))/(tvf*0.2)))

VDS4=tvf2*VDSON
VDS5=t4*VDSON


plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.plot(t1,VDS1,color='c')
plt.plot(t2,VDS2,color='r')

plt.plot(tvf1,VDS3,color='g')
plt.plot(tvf2,VDS4,color='b')
plt.plot(t4,VDS5,color='g')
plt.ylabel("VDS")
plt.xlabel("t")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
#plt.legend()
plt.show()


