from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
import matplotlib.pyplot as plt
import numpy as np

def xSplitGraph(x1, y1, x2, y2, yLabel1, yLabel2, xLabel, label1, label2, x1min, x1max, x2min, x2max):
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')

    fig.text(0.5, 0.01, xLabel, ha='center')

    color1 = 'tab:red'
    ax1.set_ylabel(yLabel1, color=color1)
    ax1.plot(x1, y1, color=color1)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.minorticks_on()

    ax3 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color2 = 'tab:blue'
    ax3.plot(x2, y2, color=color2)
    ax3.grid(which='major', axis='y')
    ax3.set_yticklabels([])
    plt.xlim(x1min, x1max)

    l2, = ax2.plot(x1, y1, color=color1, label=label1)
    ax2.tick_params(axis='y', labelcolor=color1)
    ax4 = ax2.twinx()  # instantiate a second axes that shares the same x-axis
    ax4.set_ylabel(yLabel2, color=color2)  # we already handled the x-label with ax1
    l4, = ax4.plot(x2, y2, color=color2, label=label2)
    ax4.tick_params(axis='y', labelcolor=color2)
    ax4.minorticks_on()
    ax4.grid(which='major', axis='y')
    ax2.get_yaxis().set_visible(False)

    plt.xlim(x2min, x2max)

    plt.legend([l2, l4], [label1, label2])

    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    ax1.spines['right'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax4.spines['left'].set_visible(False)

    d = .015  # how big to make the diagonal lines in axes coordinates
    # arguments to pass plot, just so we don't keep repeating them
    kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
    ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)
    ax1.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
    ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax2.plot((-d, +d), (-d, +d), **kwargs)

def giveMe4(x1, y1, x2, y2, x1p, y1p, x2p, y2p, yLabel1, yLabel2, xLabel, label1, label2, label1p, label2p, x1min, x1max, x2min, x2max, ymin, ymax):
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')

    fig.text(0.5, 0.01, xLabel, ha='center')

    color1 = 'tab:red'
    color2 = 'tab:blue'
    color1p = 'tab:orange'
    color2p = 'tab:cyan'

    ax1.set_ylabel(yLabel1, color=color1)
    ax1.plot(x1, y1, color=color1)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.plot(x1p, y1p, '--', color=color1p)
    ax1.minorticks_on()

    ax3 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax3.plot(x2, y2, color=color2)
    ax3.plot(x2p, y2p, '--', color=color2p)
    ax3.grid(which='major', axis='y')
    ax3.set_yticklabels([])

    plt.xlim(x1min, x1max)

    l2, = ax2.plot(x1, y1, color=color1, label=label1)
    ax2.tick_params(axis='y', labelcolor=color1)
    ax4 = ax2.twinx()  # instantiate a second axes that shares the same x-axis
    ax4.set_ylabel(yLabel2, color=color2)  # we already handled the x-label with ax1
    l4, = ax4.plot(x2, y2, color=color2, label=label2)
    ax4.tick_params(axis='y', labelcolor=color2)
    ax4.minorticks_on()
    ax4.grid(which='major', axis='y')
    ax2.get_yaxis().set_visible(False)

    l6, = ax2.plot(x1p, y1p, '--', color=color1p, label=label1p)
    l8, = ax4.plot(x2p, y2p, '--', color=color2p, label=label2p)

    plt.xlim(x2min, x2max)
    plt.legend([l2, l4, l6, l8], [label1, label2, label1p, label2p])
    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    ax1.spines['right'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax4.spines['left'].set_visible(False)

    d = .015  # how big to make the diagonal lines in axes coordinates
    # arguments to pass plot, just so we don't keep repeating them
    kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
    ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)
    ax1.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
    ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax2.plot((-d, +d), (-d, +d), **kwargs)

    ax3.set_ylim(ymin, ymax)
    ax4.set_ylim(ymin, ymax)

#Get SPICE data
LTR_punto3 = LTSpiceRawRead("../Spice/Draft4.raw")
LTR_punto2 = LTSpiceRawRead("../../Ejercicio 2/Spice/Draft3.raw")

time = LTR_punto3.get_trace(0)
t_s = np.abs(np.asarray(time.data))*1e6

IL_trace = LTR_punto3.get_trace("I(L1)")
VL_trace1 = LTR_punto3.get_trace("V(vl+)")
VL_trace2 = LTR_punto3.get_trace("V(vl-)")
ID_trace = LTR_punto3.get_trace("I(D1)")
Vds_trace = LTR_punto3.get_trace("V(vd)")
Vgs_trace = LTR_punto3.get_trace("V(vg)")
Ids_trace = LTR_punto3.get_trace("Id(M1)")
Ig_trace = LTR_punto3.get_trace("Ig(M1)")
Vout_trace = LTR_punto3.get_trace("V(vout)")
Vtrig_trace = LTR_punto3.get_trace("V(vtrig)")

IL_s = np.asarray(IL_trace.data)
VL_s = np.asarray(VL_trace1.data) - np.asarray(VL_trace2.data)
ID_s = np.asarray(ID_trace.data)

Vds_s = np.asarray(Vds_trace.data)
Ids_s = np.asarray(Ids_trace.data)
Vgs_s = np.asarray(Vgs_trace.data)
Ig_s = np.asarray(Ig_trace.data)

Vout_s = np.asarray(Vout_trace.data)
Vtrig_s = np.asarray(Vtrig_trace.data)

time = LTR_punto2.get_trace(0)
t_s_2 = np.abs(np.asarray(time.data))*1e6

IDs_ej2 = np.asarray(LTR_punto2.get_trace("I(S1)").data)
Vds_ej2 = np.asarray(LTR_punto2.get_trace("V(vd)").data)

#VGS E IG CARGA Y DESCARGA
# xSplitGraph(t_s, Vgs_s, t_s, Ig_s*1e3, '$V_{gs} \ [V]$', '$I_g \ [mA]$', 'Tiempo $[\mu s]$', '$V_{gs}$', '$I_g$', 7, 9, 32, 35)
giveMe4(t_s, Vgs_s, t_s, Ig_s*1e3, t_s_2, Vds_ej2, t_s_2, IDs_ej2*1e3, '$V_{gs} \ [V]$', '$I_g \ [mA]$', 'Tiempo $[\mu s]$', '$V_{gs}$ con MOS', '$I_g$ con MOS', '$V_{gs}$ llave ideal', '$I_g$ llave ideal', 7, 9, 32, 35, -100, 1000)
plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\ig-vgs.png')
plt.show()

#VDS E IDS CARGA Y DESCARGA
xSplitGraph(t_s, Vds_s, t_s, Ids_s, '$V_{ds} \ [V]$', '$I_{ds} \ [A]$', 'Tiempo $[\mu s]$', "$V_{ds}$", "$I_{ds}$", 7, 9, 32, 35)
plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\ig-vgs.png')
plt.show()

#IL
plt.figure(num=1, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$I_L \ [mA]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t_s,IL_s*1e3,color='b', label="LTSpice")
plt.xlim(0, 50)
plt.ylim(250, 850)
plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\il.png')
plt.show()

#VL
plt.figure(num=2, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$V_L \ [V]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t_s,VL_s,color='b', label="LTSpice")
plt.xlim(0, 50)
plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\ vl.png')
plt.show()

#ID
plt.figure(num=3, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$I_D \ [mA]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t_s,ID_s*1e3,color='b', label="LTSpice")
plt.xlim(0, 50)
plt.ylim(-1000, 1000)
plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\id.png')
plt.show()

#Vout
plt.figure(num=4, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
plt.ylabel("$V_{Out} \ [V]$")
plt.xlabel("Tiempo $[\mu s]$")
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(t_s,Vout_s,color='b', label="LTSpice")
plt.xlim(0, 50)
plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\ vout.png')
plt.show()

