
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
VDSO=12
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




t1= np.linspace(0,toff,100)
t2= np.linspace(toff,toff+trv,100)
t3= np.linspace(toff+trv,toff+trv+tfi,100)
t4= np.linspace(toff+trv+tfi,tend,100)
#tvf1=np.linspace(tri+ton,tvf*1+tri+ton,int(100*1))
#tvf2=np.linspace(tvf*0.5+tri+ton,tvf+tri+ton,int(100*0.5))


VGS=[]

VGS1=(VGSO*(np.exp(-t1/tau2)))

VGS2=VGSIO+0*t2

delta=trv+toff


VGS3= (VGSIO*(np.exp(-(t3-delta)/tau1)))


VGS4=(VGSIO*(np.exp(-(t4-delta)/tau1)))


IGS=[]

IGS1=-(IGSO*(np.exp(-t1/tau2)))

IGS2=-IGSIO+0*t2

IGS3= -(IGSIO*(np.exp(-(t3-delta)/tau1)))

IGS4=-(IGSIO*(np.exp(-(t4-delta)/tau1)))


IDS=[]

IDS1=ION+t1*0

IDS2=ION+t2*0

IDS3=(ION*(1-(t3-toff-trv)/(tfi)))

IDS4=t4*0



VDS=[]


VDS1=(VDSON+0*(np.exp(-t1/tau1)))

VDS2=(((VDSO-VDSON)*(t2-(toff))/(trv)))+VDSON

VDS3=VDSO+t3*0

VDS5=t4*0+VDSO


fig, ax1 = plt.subplots(figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')

ax1.set_xlabel('time (s)')
ax1.set_ylabel('Vds')
ax1.plot(t1, VDS1, color='c')
ax1.plot(t2, VDS2, color='r')
ax1.plot(t3, VDS3, color='g')
ax1.plot(t4, VDS5, color='g',label='VDS')
plt.legend()




ax2 = ax1.twinx()
ax2.set_ylabel('Ids')
ax2.plot(t1,IDS1,'--',color='c')
ax2.plot(t2,IDS2,'--',color='r')
ax2.plot(t3,IDS3,'--',color='g',label='IDS')
ax2.plot(t4,IDS4,'--',color='g')

plt.xlabel("t")
plt.legend()
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.show()
#fig.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.show()



fig2, ax3 = plt.subplots(figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
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
ax4.set_ylabel('Ig')

ax4.plot(t1,IGS1,'--',color='c')
ax4.plot(t2,IGS2,'--',color='r')
ax4.plot(t3,IGS3,'--',color='g')
ax4.plot(t4,IGS4,'--',color='b',label='IG')#, label='')
plt.legend()
plt.xlabel("t")
plt.show()

