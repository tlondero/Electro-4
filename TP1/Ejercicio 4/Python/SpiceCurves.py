from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
import matplotlib.pyplot as plt
import numpy as np

def giveMe4(x1, y1, x2, y2, x1p, y1p, x2p, y2p, yLabel1, yLabel2, xLabel, label1, label2, label1p, label2p, xlim = [], ylim1 = [], ylim2 = []):
    fig, ax1 = plt.subplots(sharey=True, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')

    color1 = 'tab:red'
    color2 = 'tab:blue'
    color1p = 'tab:orange'
    color2p = 'tab:cyan'

    ax1.set_xlabel(xLabel)
    ax1.set_ylabel(yLabel1, color=color1)
    l1, = ax1.plot(x1, y1, color=color1, label=label1)
    ax1.tick_params(axis='y', labelcolor=color1)
    l2, = ax1.plot(x1p, y1p, '--', color=color1p, label=label1p)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.set_ylabel(yLabel2, color=color2)
    ax2.tick_params(axis='y', labelcolor=color2)
    l3, = ax2.plot(x2, y2, color=color2, label=label2)
    l4, = ax2.plot(x2p, y2p, '--', color=color2p, label=label2p)

    plt.minorticks_on()
    plt.grid(which='major')

    plt.legend([l1, l2, l3, l4], [label1, label2, label1p, label2p])
    if(xlim != []):
        plt.xlim(xlim[0], xlim[1])
    if (ylim1 != []):
        ax1.set_ylim(ylim1[0], ylim1[1])
    if (ylim2 != []):
        ax2.set_ylim(ylim2[0], ylim2[1])

    fig.tight_layout()

#Get SPICE data

LTR_snubber_sin = LTSpiceRawRead("../Spice/Draft4.raw")
LTR_snubber_con = LTSpiceRawRead("../Spice/Draft4_snubber.raw")

t_sin = np.abs(np.asarray(LTR_snubber_sin.get_trace(0).data))*1e6
t_con = np.abs(np.asarray(LTR_snubber_con.get_trace(0).data))*1e6

Vds_sin = np.asarray(LTR_snubber_sin.get_trace("V(vd)").data)
Vds_con = np.asarray(LTR_snubber_con.get_trace("V(vd)").data)

Ids_sin = np.asarray(LTR_snubber_sin.get_trace("Id(M1)").data)*1e3
Ids_con = np.asarray(LTR_snubber_con.get_trace("Id(M1)").data)*1e3

###########################################
##        COMPARACIÓN De todo            ##
###########################################

giveMe4(t_sin, Vds_sin, t_sin, Ids_sin, t_con, Vds_con, t_con, Vds_con, 'Tensión [V]', 'Corriente [mA]', 'Tiempo $[\mu s]$', 'Tensión sin snubber',
        'Tensión con snubber', 'Corriente sin snubber', 'Corriente con snubber')
plt.savefig('..\..\Tex\Ejercicio-4\ImagenesEjercicio-4\con-y-sin-snubber.png')
plt.show()


color1 = 'tab:red'
color2 = 'tab:orange'

###########################################
##            COMPARACIÓN Vds            ##
###########################################

plt.figure(num=6, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Tensión [V]")
plt.xlabel('Tiempo $[\mu s]$')

plt.minorticks_on()
plt.grid(which='major')

l1, = plt.plot(t_sin, Vds_sin, color=color1)
l2, = plt.plot(t_con, Vds_con, color=color2)

plt.legend([l1, l2], ["Sin snubber", "Con snubber"])

plt.tight_layout()

plt.savefig('..\..\Tex\Ejercicio-4\ImagenesEjercicio-4\comparacion-vds.png')
plt.show()

###########################################
##            COMPARACIÓN Ids            ##
###########################################

plt.figure(num=6, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("Corriente [mA]")
plt.xlabel('Tiempo $[\mu s]$')

plt.minorticks_on()
plt.grid(which='major')

l1, = plt.plot(t_sin, Ids_sin, color=color1)
l2, = plt.plot(t_con, Ids_con, color=color2)

plt.legend([l1, l2], ["Sin snubber", "Con snubber"])

plt.tight_layout()

plt.savefig('..\..\Tex\Ejercicio-4\ImagenesEjercicio-4\comparacion-ids.png')
plt.show()