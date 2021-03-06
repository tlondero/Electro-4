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

compSnubb = False

if compSnubb:

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

else:
    ###########################################
    ##               Potencia                ##
    ###########################################


    # #Get SPICE data
    LTR_ccm = LTSpiceRawRead("../Spice/Draft4_CCM.raw")
    LTR_pot = LTSpiceRawRead("../Spice/Draft4_pot.raw")
    LTR_snub = LTSpiceRawRead("../Spice/Draft4_snubber_pot.raw")

    t_ccm = np.abs(np.asarray(LTR_ccm.get_trace(0).data))*1e6
    t_pot = np.abs(np.asarray(LTR_pot.get_trace(0).data))*1e6
    t_snub = np.abs(np.asarray(LTR_snub.get_trace(0).data))*1e6

    pot_ccm = np.asarray(LTR_ccm.get_trace("V(vd)").data)*np.asarray(LTR_ccm.get_trace("Id(M1)").data) + np.asarray(LTR_ccm.get_trace("V(vg)").data)*np.asarray(LTR_ccm.get_trace("Ig(M1)").data)
    pot_pot = np.asarray(LTR_pot.get_trace("V(vd)").data)*np.asarray(LTR_pot.get_trace("Id(M1)").data) + np.asarray(LTR_pot.get_trace("V(vg)").data)*np.asarray(LTR_pot.get_trace("Ig(M1)").data)
    pot_snub = np.asarray(LTR_snub.get_trace("V(vd)").data)*np.asarray(LTR_snub.get_trace("Id(M1)").data) + np.asarray(LTR_snub.get_trace("V(vg)").data)*np.asarray(LTR_snub.get_trace("Ig(M1)").data)
    pot_snub_r = (np.asarray(LTR_snub.get_trace("V(vd)").data) - np.asarray(LTR_snub.get_trace("V(p001)").data))*np.asarray(LTR_snub.get_trace("I(R7)").data)

    color1 = 'tab:blue'
    color2 = 'tab:green'
    color3 = 'tab:red'
    color4 = 'tab:orange'

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')
    fig.subplots_adjust(hspace=0.05)  # adjust space between axes

    l1, = ax1.plot(t_ccm, pot_ccm, color=color1)
    l1, = ax2.plot(t_ccm, pot_ccm, color=color1)

    l2, = ax1.plot(t_pot, pot_pot, color=color2)
    l2, = ax2.plot(t_pot, pot_pot, color=color2)

    l3, = ax1.plot(t_snub, pot_snub, color=color3)
    l3, = ax2.plot(t_snub, pot_snub, color=color3)

    l4, = ax1.plot(t_snub, pot_snub_r, '--', color=color4)
    l4, = ax2.plot(t_snub, pot_snub_r, '--', color=color4)

    plt.text(-1.9, 21, 'Potencia [W]', va='center', rotation='vertical')

    ax1.set_ylim(70, 85)  # outliers only
    ax2.set_ylim(0, 20)  # most of the data

    # hide the spines between ax and ax2
    ax1.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.xaxis.tick_top()
    ax1.tick_params(labeltop=False)  # don't put tick labels at the top
    ax2.xaxis.tick_bottom()

    d = .5  # proportion of vertical to horizontal extent of the slanted line
    kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
                  linestyle="none", color='k', mec='k', mew=1, clip_on=False)
    ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
    ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

    ax1.legend([l1, l2, l3, l4], ["CCM", "Sin snubber", "Con snubber", "Resistencia del snubber"])

    ax1.minorticks_on()
    ax1.grid(which='major')
    ax2.minorticks_on()
    ax2.grid(which='major')

    plt.xlabel('Tiempo $[\mu s]$')
    #ax1.text(-1.75, 85, 'Potencia [W]', va='top', rotation='vertical')
    plt.tight_layout()
    fig.subplots_adjust(hspace=0.05)
    plt.savefig('..\..\Tex\Ejercicio-4\ImagenesEjercicio-4\potencias-crop.png')

    plt.show()