import matplotlib.pyplot as plt
import numpy as np
import pandas as pnd

#CSV PARSER

df = pnd.read_csv('../Mediciones/Pin9-Vref2V.csv', sep=',')
t = np.asarray(df["x-axis"])
t = (t - t[0])*(1E6)
pin9 = np.asarray(pnd.DataFrame(df["1"]).ewm(com=100).mean())

#TENSIÓN DE COM
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
#plt.grid(which='minor')
plt.plot(t,pin9, label="Tensión de Pin 9")
plt.legend()
plt.xlim(0, 50)
#plt.savefig('..\Tex\ParteIV\ImagenesParteIV\Vcom.png')
plt.show()