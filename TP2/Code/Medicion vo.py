import matplotlib.pyplot as plt
import numpy as np
import pandas as pnd

#CSV PARSER




#TENSIÓN DE SALIDA
df = pnd.read_csv('../Mediciones/1127/Vo-Vref1127V_v.csv', sep='\t')
t = np.asarray(df["Time (s)"])
t = (t - t[0])*(1E6)

pin9 = np.asarray(df["Channel 1 (V)"])#+0.014
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
vline1=t*0+3.075
vline2=t*0+2.925



plt.plot(t,pin9, label="Tensión de salida")
plt.plot(t,vline2,'--' )
plt.plot(t,vline1,'--')
plt.savefig('..\Tex\ParteIV\ImagenesParteIV\Vout_vieja.png')
plt.legend()
plt.xlim(0, 50)
plt.show()
