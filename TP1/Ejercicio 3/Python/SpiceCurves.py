from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
import matplotlib.pyplot as plt
import numpy as np

def giveMe4WithCrop(x1, y1, x2, y2, x1p, y1p, x2p, y2p, yLabel1, yLabel2, xLabel, label1, label2, label1p, label2p, xlim1 = [], xlim2 = [], ylim1 = [], ylim2 = []):
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

    if(xlim1 != []):
        plt.xlim(xlim1[0], xlim1[1])

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

    if (xlim2 != []):
        plt.xlim(xlim2[0], xlim2[1])
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

    if (ylim1 != []):
        ax3.set_ylim(ylim1[0], ylim1[1])
        ax4.set_ylim(ylim1[0], ylim1[1])
    if (ylim2 != []):
        ax1.set_ylim(ylim2[0], ylim2[1])
        ax2.set_ylim(ylim2[0], ylim2[1])

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

def giveMe2WithCrop(x1, y1, x1p, y1p, yLabel, xLabel, label1, label1p, xlim1 = [], xlim2 = [], ylim = []):

    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')

    fig.text(0.5, 0.01, xLabel, ha='center')

    color1 = 'tab:red'
    color1p = 'tab:orange'

    ax1.set_ylabel(yLabel, color=color1)
    ax1.plot(x1, y1, color=color1)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.plot(x1p, y1p, '--', color=color1p)
    ax1.grid(which='major', axis='y')
    ax1.minorticks_on()

    if(xlim1 != []):
        ax1.set_xlim(xlim1[0], xlim1[1])

    l1, = ax2.plot(x1, y1, color=color1, label=label1)
    ax2.tick_params(axis='y', labelcolor=color1)
    ax2.minorticks_on()
    ax2.grid(which='major', axis='y')
    ax2.yaxis.tick_right()

    l1p, = ax2.plot(x1p, y1p, '--', color=color1p, label=label1p)

    if (xlim2 != []):
        plt.xlim(xlim2[0], xlim2[1])
    plt.legend([l1, l1p], [label1, label1p])
    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    ax1.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)

    d = .015  # how big to make the diagonal lines in axes coordinates
    # arguments to pass plot, just so we don't keep repeating them
    kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
    ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)
    ax1.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
    ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax2.plot((-d, +d), (-d, +d), **kwargs)

    if (ylim != []):
        ax1.set_ylim(ylim[0], ylim[1])
        ax2.set_ylim(ylim[0], ylim[1])


#Get SPICE data
LTR_punto3 = LTSpiceRawRead("../Spice/Draft4.raw")
LTR_punto2 = LTSpiceRawRead("../../Ejercicio 2/Spice/Draft3.raw")
LTR_punto1 = LTSpiceRawRead("../../Ejercicio 1/Spice/Draft1.raw")

t_ej3 = np.abs(np.asarray(LTR_punto3.get_trace(0).data))*1e6
t_ej2 = np.abs(np.asarray(LTR_punto2.get_trace(0).data))*1e6
t_ej1 = np.abs(np.asarray(LTR_punto1.get_trace(0).data))*1e6

show3con2 = True
show3con1 = False

##########################################
##      COMPARACIÓN PUNTO 3 CON 2       ##
##########################################

#VDS E IDS CARGA Y DESCARGA
Vds_ej3 = np.asarray(LTR_punto3.get_trace("V(vd)").data)
Ids_ej3 = np.asarray(LTR_punto3.get_trace("Id(M1)").data)

if show3con2:
    Vds_ej2 = np.asarray(LTR_punto2.get_trace("V(vd)").data)
    Ids_ej2 = np.asarray(LTR_punto2.get_trace("I(S1)").data)

    giveMe4WithCrop(t_ej3-1, Vds_ej3, t_ej3-1, Ids_ej3*1e3, t_ej2, Vds_ej2, t_ej2, Ids_ej2*1e3, '$V_{DS} \ [V]$', '$I_{DS} \ [mA]$', 'Tiempo $[\mu s]$', '$V_{DS}$ con MOS', '$I_{DS}$ con MOS', '$V_{DS}$ llave ideal', '$I_{DS}$ llave ideal', [16, 18], [22, 27], [-150, 2500])
    plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\ids-vds-2v3.png')
    plt.show()

#VGS E IG CARGA Y DESCARGA
Vgs_ej3 = np.asarray(LTR_punto3.get_trace("V(vg)").data)
Ig_ej3 = np.asarray(LTR_punto3.get_trace("Ig(M1)").data)

if show3con2:
    Vgs_ej2 = np.asarray(LTR_punto2.get_trace("V(vtrig)").data)
    Ig_ej2 = np.asarray(LTR_punto2.get_trace("I(V1)").data)

    giveMe4WithCrop(t_ej3, Vgs_ej3, t_ej3, Ig_ej3*1e3, t_ej2-(25.5e-6), Vgs_ej2*12/5, t_ej2-(25.5e-6), Ig_ej2*1e3, '$V_{GS} \ [V]$', '$I_G \ [mA]$', 'Tiempo $[\mu s]$', '$V_{GS}$ con MOS', '$I_G$ con MOS', '$V_{GS}$ llave ideal', '$I_G$ llave ideal', [16, 19], [22, 27], [-125, 100])
    plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\ig-vgs-2v3.png')
    plt.show()

#IL y VL
Vl_ej3 = np.asarray(LTR_punto3.get_trace("V(vl+)").data) - np.asarray(LTR_punto3.get_trace("V(vl-)").data)
Il_ej3 = np.asarray(LTR_punto3.get_trace("I(L1)").data)

if show3con2:
    Vl_ej2 = np.asarray(LTR_punto2.get_trace("V(vl+)").data) - np.asarray(LTR_punto2.get_trace("V(vl-)").data)
    Il_ej2 = np.asarray(LTR_punto2.get_trace("I(L1)").data)

    giveMe4(t_ej3, Vl_ej3, t_ej3, Il_ej3*1e3, t_ej2, Vl_ej2, t_ej2, Il_ej2*1e3, '$V_{L} \ [V]$', '$I_L \ [mA]$', 'Tiempo $[\mu s]$', '$V_{L}$ con MOS', '$V_{L}$ llave ideal', '$I_L$ con MOS', '$I_L$ llave ideal', [0, 50], ylim2=[0, 850])
    plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\il-vl-2v3.png')
    plt.show()

#ID y VD
Vd_ej3 = np.asarray(LTR_punto3.get_trace("V(vd)").data) - np.asarray(LTR_punto3.get_trace("V(vout)").data)
Id_ej3 = np.asarray(LTR_punto3.get_trace("I(D1)").data)

if show3con2:
    Vd_ej2 = np.asarray(LTR_punto2.get_trace("V(vd)").data) - np.asarray(LTR_punto2.get_trace("V(vout)").data)
    Id_ej2 = np.asarray(LTR_punto2.get_trace("I(D1)").data)

    giveMe4(t_ej3, Vd_ej3, t_ej3, Id_ej3, t_ej2, Vd_ej2, t_ej2, Id_ej2, '$V_{D} \ [V]$', '$I_D \ [A]$', 'Tiempo $[\mu s]$', '$V_{D}$ con MOS', '$I_D$ con MOS', '$V_{D}$ llave ideal', '$I_D$ llave ideal', [0, 50], ylim2=[-2.5, 0.85])
    plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\id-vd-2v3.png')
    plt.show()

##########################################
##      COMPARACIÓN PUNTO 3 CON 1       ##
##########################################

#VDS E IDS CARGA Y DESCARGA
if show3con1:
    Vds_ej1 = np.asarray(LTR_punto1.get_trace("V(vd)").data)
    Ids_ej1 = np.asarray(LTR_punto1.get_trace("Id(M1)").data)

    giveMe2WithCrop(t_ej3, Vds_ej3, t_ej1, Vds_ej1, '$V_{DS} \ [V]$','Tiempo $[\mu s]$','$V_{DS}$ con carga', '$V_{DS}$ sin carga', [16, 18], [22, 27], [0, 25])
    plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\ids-vds-1v3.png')
    plt.show()

#VGS E IG CARGA Y DESCARGA
if show3con1:
    Vgs_ej1 = np.asarray(LTR_punto1.get_trace("V(vg)").data)
    Ig_ej1 = np.asarray(LTR_punto1.get_trace("Ig(M1)").data)

    giveMe4WithCrop(t_ej3-0.75, Vgs_ej3, t_ej3-0.75, Ig_ej3*1e3, t_ej1, Vgs_ej1, t_ej1, Ig_ej1*1e3, '$V_{GS} \ [V]$', '$I_G \ [mA]$', 'Tiempo $[\mu s]$', '$V_{GS}$ con carga', '$I_G$ con carga', '$V_{GS}$ sin carga', '$I_G$ sin carga', [16, 18], [22, 27], [-125, 100])
    plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\ig-vgs-1v3.png')
    plt.show()

#IL y VL
if show3con1:
    Vl_ej1 = np.asarray(LTR_punto1.get_trace("V(vl+)").data) - np.asarray(LTR_punto1.get_trace("V(vd)").data)
    Il_ej1 = np.asarray(LTR_punto1.get_trace("I(L1)").data)

    giveMe4(t_ej3, Vl_ej3, t_ej3, Il_ej3, t_ej1, Vl_ej1, t_ej1, Il_ej1, '$V_{L} \ [V]$', '$I_L \ [A]$', 'Tiempo $[\mu s]$', '$V_{L}$ con carga', '$V_L$ sin carga', '$I_{L}$ con carga', '$I_L$ sin carga', [0, 50])
    plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\il-vl-1v3.png')
    plt.show()

#ID y VD
if show3con1:
    Vd_ej1 = np.asarray(LTR_punto1.get_trace("V(vd)").data) - np.asarray(LTR_punto1.get_trace("V(vd-)").data)
    Id_ej1 = np.asarray(LTR_punto1.get_trace("I(D1)").data)

    giveMe4(t_ej3, Vd_ej3, t_ej3, Id_ej3, t_ej1, Vd_ej1, t_ej1, Id_ej1, '$V_{D} \ [V]$', '$I_D \ [A]$', 'Tiempo $[\mu s]$', '$V_{D}$ con carga', '$V_D$ sin carga', '$I_{D}$ con carga', '$I_D$ sin carga', [0, 50], [-500, 850])
    plt.savefig('..\..\Tex\Ejercicio-3\ImagenesEjercicio-3\id-vd-1v3.png')
    plt.show()