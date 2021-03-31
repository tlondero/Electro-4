
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
VD0=13

IGSO=12/RG
ION= VGSO/(RL+RDS)*D
IOFF=ION
IGSIO=65E-3

VDSON=RDS*ION
deltaQ=7.3E-9#fijate que en el spice dice otra cosa

#Constantes de tiempo

tau1=RG*Cgs_plus_cgd1
tau2=RG*Cgs_plus_cgd2

ton=-tau1*np.log(1-VTH/VGSO)#30.41E-9

tri=-tau1*np.log((VGSO-VGSIO)/(VGSO)) - ton#5.198e-08-ton
tvf=deltaQ*RG/(VGSO-VGSIO) #1.7358e-07-tri-ton

tend=9.7358e-07




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


IGS=[]

IGS1=(IGSO*(np.exp(-t1/tau1)))

IGS2=(IGSO*(np.exp(-t2/tau1)))

IGS3= IGSIO+0*t3


IGS4=(IGSIO*(np.exp(-(t4-delta)/tau2)))






IDS=[]

IDS1=(0*(np.exp(-t1/tau1)))

IDS2=(ION*(t2-ton)/(tri))

IDS3=ION+t3*0

IDS4=ION+t4*0



VDS=[]


VDS1=(VD0+0*(np.exp(-t1/tau1)))

VDS2=VDS1

VDS3=((VD0)-((VD0-VDSON)*(tvf1-(ton+tri))/(tvf)))

#VDS4=tvf2*VDSON
VDS5=t4*0+VDSON


fig, ax1 = plt.subplots()
ax1.set_xlabel('time (s)')
ax1.set_ylabel('Vds')
ax1.plot(t1, VDS1, color='c')
ax1.plot(t2, VDS2, color='r')
ax1.plot(tvf1, VDS3, color='g')
ax1.plot(t4, VDS5, color='g',label='VDS')
plt.legend()




ax2 = ax1.twinx()
ax2.set_ylabel('Ids')
ax2.plot(t1,IDS1,'--',color='c')
ax2.plot(t2,IDS2,'--',color='r')
ax2.plot(t3,IDS3,'--',color='g',label='IDS')
ax2.plot(t4,IDS3,'--',color='g')

plt.xlabel("t")
plt.legend()
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.show()
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()



fig2, ax3 = plt.subplots()
ax3.set_xlabel('time (s)')
ax3.set_ylabel('Vgs')

ax3.plot(t1,VGS1,color='c')
ax3.plot(t2,VGS2,color='r')
ax3.plot(t3,VGS3,color='g')
ax3.plot(t4,VGS4,color='b',label='VGS')#, label='')

plt.legend()
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')




ax4 = ax3.twinx()
ax4.set_ylabel('Igs')

ax4.plot(t1,IGS1,'--',color='c')
ax4.plot(t2,IGS2,'--',color='r')
ax4.plot(t3,IGS3,'--',color='g')
ax4.plot(t4,IGS4,'--',color='b',label='IGS')#, label='')
plt.legend()
plt.xlabel("t")
plt.show()

