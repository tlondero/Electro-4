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




from mpl_toolkits.mplot3d import Axes3D

import random
from matplotlib import cm
def fun(Vx, Rx):
    return (2*Vx**2 / Rx) * 1/((2*Vx**2 / Rx) + (C*Vc**2 *Fsw/2)+Fsw/2 * Vsw * (Vx/(Rx*(1-D)) * N2/N1 - Vx/(2*L2*Fsw) * (1-D) * N1/N2) * tsw2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
y = np.arange(0.71, 50, 0.5)
x  = np.arange(0.7, 3.1, 0.05)
X, Y = np.meshgrid(x, y)
zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)
my_col = cm.jet(Z/np.amax(Z))
ax.plot_surface(X, Y, Z*100,facecolors = my_col,
        linewidth=0, antialiased=False)

ax.set_xlabel('$V_{out}$ [V]')
ax.set_ylabel('$R_{L}$ [$\Omega$] ')
ax.set_zlabel('$\eta $[%]')

plt.show()