#
# * =============================================================================
# * DEPENDÊNCIAS
# * =============================================================================

# ? -----------------------------------------------------------------------------
# ?         BIBLIOTECAS
# ? -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
from pathlib import Path as path
from matplotlib.ticker import AutoMinorLocator
import numpy as np


# * =============================================================================
# * FUNÇÕES DE CRIAÇÃO DE GRÁFICOS
# * =============================================================================


def plot(
    save, x, y, save_name="", titulo_x="X", titulo_y="Y", tam_fonte=14, espessura=2.5
):
    """Função responsável por plotar gráficos com o estilo padrão LaTeX/Científico."""
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
    ax.set_title("", fontsize=tam_fonte + 2, pad=15)
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
        folderData = path("figures")
        folderData.mkdir(parents=True, exist_ok=True)
        plt.savefig(
            folderData / f"{save_name.replace(' ', '')}.pdf",
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
    save_name="",
    titulo_x="X",
    titulo_y="Y",
    tam_fonte=14,
    espessura=2.5,
):
    """Função responsável por plotar gráficos sobrepostos com o estilo padrão LaTeX/Científico."""
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
    ax.plot(x2, y2, linewidth=espessura, color="black", linestyle="--", label=label2)
    ax.plot(x3, y3, linewidth=espessura, color="black", linestyle=":", label=label3)
    ax.set_title("", fontsize=tam_fonte + 2, pad=15)
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
    ax.legend(
        fontsize=tam_fonte - 2,
        frameon=False,
        fancybox=False,
        shadow=False,
        edgecolor="black",
        loc="best",
    )
    plt.tight_layout()
    if save == True:
        folderData = path("figures")
        folderData.mkdir(parents=True, exist_ok=True)
        plt.savefig(
            folderData / f"{save_name.replace(' ','')}.pdf",
            bbox_inches="tight",
            dpi=600,
            facecolor="white",
            transparent=False,
        )
    plt.show()


def elipse_plot(
    save,
    x_list,
    y_list,
    z_matrix,
    levels,
    save_name="",
    titulo_x=r"$\Omega_M$",
    titulo_y=r"$\Omega_{EE}$",
    tam_fonte=14,
):
    """
    Função para plotar contornos de confiança (elipses) no estilo padrão LaTeX.
    Recebe x_list e y_list (eixos da malha) e z_matrix (matriz de Chi2).
    """
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
    fig, ax = plt.subplots(figsize=(8, 7), dpi=100)
    contorno = ax.contour(
        x_list,
        y_list,
        z_matrix.T,
        levels=levels,
        colors=["#1f77b4", "#ff7f0e", "#2ca02c"],
        linewidths=2.0,
    )
    fmt = {levels[0]: r"1$\sigma$", levels[1]: r"2$\sigma$", levels[2]: r"3$\sigma$"}
    ax.clabel(contorno, inline=True, fontsize=tam_fonte - 4, fmt=fmt)
    x_plano = np.linspace(min(x_list), max(x_list), 100)
    ax.plot(
        x_plano,
        1 - x_plano,
        color="black",
        linestyle="--",
        alpha=0.6,
        label="Universo Plano",
    )
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
    idx_m, idx_ee = np.unravel_index(np.argmin(z_matrix), z_matrix.shape)
    ax.plot(x_list[idx_m], y_list[idx_ee], "rx", markersize=8, label="Best Fit")
    ax.legend(fontsize=tam_fonte - 2, frameon=False)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("black")
    plt.tight_layout()
    if save == True:
        folderData = path("figures")
        folderData.mkdir(parents=True, exist_ok=True)
        plt.savefig(
            folderData / f"{save_name.replace(' ', '')}.pdf",
            bbox_inches="tight",
            dpi=600,
            facecolor="white",
            transparent=False,
        )
    plt.show()
