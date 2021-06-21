import matplotlib.pyplot as plt
import numpy as np
import pandas as pnd

#TENSIÓN DE osc
#df = pnd.read_csv('../Mediciones/1127/Pin4-Vref1127V.csv', sep=',')
Rl = 6.75
Vo=np.linspace(0.8,       3,       num = 100,    endpoint = True)
C=35e-9
Fsw=100e3
Vc=21
N2=3
N1=1
tsw2=300e-9
L2=4.444e-6
D=0.3
Vsw=Vc

Eff = (2*Vo**2 / Rl) * 1/((2*Vo**2 / Rl) + (C*Vc**2 *Fsw/2)+Fsw/2 * Vsw * (Vo/(Rl*(1-D)) * N2/N1 - Vo/(2*L2*Fsw) * (1-D) * N1/N2) * tsw2)



plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel(" $\eta$ [%]")
plt.xlabel("Tensión de salida $[V]$")
plt.minorticks_on()
plt.grid(which='major')
plt.stem([6.75], [70.355],linefmt='red', markerfmt='D', use_line_collection = True,label='70.35%')
plt.plot(Vo,Eff*100, label="Eficiencia en función de la tensión de salida")
plt.legend()
#plt.xlim(0, 50)
plt.savefig('..\Tex\ParteII\ImagenesParteII\VEff.png')
plt.show()