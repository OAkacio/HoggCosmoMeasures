#
# * =============================================================================
# * DEPENDÊNCIAS
# * =============================================================================

# ? -----------------------------------------------------------------------------
# ?         BIBLIOTECAS
# ? -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
import random
from pathlib import Path as path
from matplotlib.ticker import AutoMinorLocator


# * =============================================================================
# * FUNÇÕES DE CRIAÇÃO DE GRÁFICOS
# * =============================================================================


def plot(
    save, x, y, titulo="", titulo_x="X", titulo_y="Y", tam_fonte=14, espessura=1.5
):
    plt.rcParams.update(
        {
            "font.family": "serif",
            "mathtext.fontset": "dejavuserif",
            "axes.labelsize": tam_fonte,
            "font.size": tam_fonte,
            "xtick.labelsize": tam_fonte - 2,
            "ytick.labelsize": tam_fonte - 2,
            "axes.linewidth": 1.2,
        }
    )
    fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
    ax.plot(x, y, linewidth=espessura, color="black", linestyle="-")
    if titulo != "":
        ax.set_title(titulo, fontsize=tam_fonte + 2, pad=15)
    ax.set_xlabel(titulo_x, labelpad=8)
    ax.set_ylabel(titulo_y, labelpad=8)
    ax.tick_params(
        which="major", direction="in", length=6, width=1.2, top=True, right=True
    )
    ax.tick_params(
        which="minor", direction="in", length=3, width=1.0, top=True, right=True
    )
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("black")
    ax.grid(False)
    plt.tight_layout()
    if save == True:
        if titulo == "":
            titulo = f"graph{random.randint(0,100000)}"
        folderData = path("figures")
        folderData.mkdir(parents=True, exist_ok=True)
        plt.savefig(
            folderData / f"{titulo.replace(' ', '')}.png",
            bbox_inches="tight",
            dpi=600,
            facecolor="white",
            transparent=False,
        )
    plt.show()


def ppplot(
    save,
    x1,
    y1,
    x2,
    y2,
    x3,
    y3,
    label1="Modelo1",
    label2="Modelo2",
    label3="Modelo3",
    titulo="",
    titulo_x="X",
    titulo_y="Y",
    tam_fonte=14,
    espessura=1.5,
):
    plt.rcParams.update(
        {
            "font.family": "serif",
            "mathtext.fontset": "dejavuserif",
            "axes.labelsize": tam_fonte,
            "font.size": tam_fonte,
            "xtick.labelsize": tam_fonte - 2,
            "ytick.labelsize": tam_fonte - 2,
            "axes.linewidth": 1.2,
        }
    )
    fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
    ax.plot(x1, y1, linewidth=espessura, color="black", linestyle="-", label=label1)
    ax.plot(x2, y2, linewidth=espessura, color="blue", linestyle="--", label=label2)
    ax.plot(x3, y3, linewidth=espessura, color="red", linestyle=":", label=label3)
    if titulo != "":
        ax.set_title(titulo, fontsize=tam_fonte + 2, pad=15)
    ax.set_xlabel(titulo_x, labelpad=8)
    ax.set_ylabel(titulo_y, labelpad=8)
    ax.tick_params(
        which="major", direction="in", length=6, width=1.2, top=True, right=True
    )
    ax.tick_params(
        which="minor", direction="in", length=3, width=1.0, top=True, right=True
    )
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    # 5. Fechando a caixa do gráfico
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("black")
    ax.grid(False)
    ax.legend(
        fontsize=tam_fonte - 2,
        frameon=True,
        fancybox=False,
        shadow=False,
        edgecolor="black",
        loc="best",
    )
    plt.tight_layout()
    if save == True:
        if titulo == "":
            titulo = f"graph{random.randint(0,100000)}"
        folderData = path("figures")
        folderData.mkdir(parents=True, exist_ok=True)
        plt.savefig(
            folderData / f"{titulo.replace(' ','')}.png",
            bbox_inches="tight",
            dpi=600,
            facecolor="white",
            transparent=False,
        )
    plt.show()
