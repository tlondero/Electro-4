
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import math
#componentes
RG=100
L=220E-6

fsw=60E3



VGSO=12

V2=12
RL=1
RDS=0.16
Vd=1.3
IlOn=V2/(RL+RDS)
IlOff=0


#Constantes de tiempo




t1= np.linspace(0,0.0015,100)
IConstOn=IlOff-V2/(RDS+RL)
IconstOff=IlOn - Vd/RL
Il_on=(IConstOn)*np.exp(-(RDS+RL)/L *t1)+V2/(RDS+RL)
Il_off=(IconstOff)*np.exp(-RL/L * t1)
Imean=5.0645
#for i in range(len(Il_off)):
#    if(Il_off[i]< 20E-3):
#        Il_off[i]=0


fig, ax1 = plt.subplots()
ax1.set_xlabel('time (s)')
ax1.set_ylabel('I [A]')
ax1.plot(t1, Il_on, color='g',label='IL ON')
ax1.plot(t1, Il_off, color='r',label='IL OFF')
ax1.plot(t1, Imean+t1*0,'--', color='b',label='IL Mean')
plt.minorticks_on()
plt.grid()
plt.legend(loc ="lower right")
plt.show()
