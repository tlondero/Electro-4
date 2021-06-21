import matplotlib.pyplot as plt
import numpy as np
import pandas as pnd

#CSV PARSER



#TENSIÓN DE osc
df = pnd.read_csv('../Mediciones/1.45/Pin4-Vref145V.csv', sep=',')
t = np.asarray(df["Time (s)"])
t = (t - t[0])*(1E6)
pin9 = np.asarray(df["Channel 1 (V)"])
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')

plt.plot(t,pin9, label="Tensión de Oscilador")
plt.legend()
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIV\ImagenesParteIV\Vosc.png')
plt.show()

#TENSIÓN DE com
df = pnd.read_csv('../Mediciones/1.45/Pin9-Vref145V.csv', sep=',')
t = np.asarray(df["Time (s)"])
t = (t - t[0])*(1E6)
pin9 = np.asarray(df["Channel 1 (V)"])
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')

plt.plot(t,pin9, label="Tensión de compensación")
plt.legend()
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIV\ImagenesParteIV\Vcom.png')
plt.show()

#TENSIÓN DE VCsnubber
df = pnd.read_csv('../Mediciones/1.45/Vcsnubber-Vref145V.csv', sep=',')
t = np.asarray(df["Time (s)"])
t = (t - t[0])*(1E6)
pin9 = np.asarray(df["Channel 1 (V)"])
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')

plt.plot(t,pin9, label="Tensión de capacitor snubber")
plt.legend()
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIV\ImagenesParteIV\Vcsnubber.png')
plt.show()

#TENSIÓN DE drain
df = pnd.read_csv('../Mediciones/1.45/Vds-Vref145V.csv', sep=',')
t = np.asarray(df["Time (s)"])
t = (t - t[0])*(1E6)
pin9 = np.asarray(df["Channel 1 (V)"])
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')

plt.plot(t,pin9, label="Tensión de drain")
plt.legend()
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIV\ImagenesParteIV\Vds.png')
plt.show()

#TENSIÓN DE SALIDA
df = pnd.read_csv('../Mediciones/1.45/Vo-Vref145V.csv', sep=',')
t = np.asarray(df["Time (s)"])
t = (t - t[0])*(1E6)
pin9 = np.asarray(df["Channel 1 (V)"])

plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')

plt.plot(t,pin9, label="Tensión de salida   ")
plt.legend()
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIV\ImagenesParteIV\Vout.png')
plt.show()
#TENSIÓN DE referencia
df = pnd.read_csv('../Mediciones/1.45/Vref-Vref145V.csv', sep=',')
t = np.asarray(df["Time (s)"])
t = (t - t[0])*(1E6)
pin9 = np.asarray(df["Channel 1 (V)"])

plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')

plt.plot(t,pin9, label="Tensión de referencia")
plt.legend()
plt.xlim(0, 50)
plt.savefig('..\Tex\ParteIV\ImagenesParteIV\Vref.png')
plt.show()

#TENSIÓN DE secundario
df = pnd.read_csv('../Mediciones/1.45/Vsec-Vref145V.csv', sep=',')
t = np.asarray(df["Time (s)"])
t = (t - t[0])*(1E6)
pin9 = np.asarray(df["Channel 1 (V)"])
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