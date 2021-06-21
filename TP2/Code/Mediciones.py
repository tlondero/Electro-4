import matplotlib.pyplot as plt
import numpy as np
import pandas as pnd

#CSV PARSER

df = pnd.read_csv('../Mediciones/Vsec-Vref2V.csv', sep=',')
t = np.asarray(df["Time (s)"])
t = (t - t[0])*(1E6)
pin9 = np.asarray(pnd.DataFrame(df["Channel 1 (V)"]).ewm(com=100).mean())

#TENSIÓN DE COM
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')

plt.plot(t,pin9, label="Tensión de secundario")
plt.legend()
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIV\ImagenesParteIV\Vsec.png')
plt.show()