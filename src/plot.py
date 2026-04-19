# -------------------------------------------------- Bibliotecas --------------------------------------------------

import matplotlib.pyplot as plt
import random
from pathlib import Path as path

# -------------------------------------------------- Funções de Plotagem de Gráficos --------------------------------------------------


def plot(
    save, x, y, titulo="", titulo_x="X", titulo_y="Y", tam_fonte=12, espessura=2
):  # Função que plota um gráfico simples dado uma determinada quantidade de parâmetros
    plt.style.use("seaborn-v0_8-muted")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

    ax.plot(
        x, y, linewidth=espessura, color="#1a73e8", alpha=0.9, solid_capstyle="round"
    )

    ax.set_title(
        titulo, fontsize=tam_fonte + 4, fontweight="bold", pad=20, color="#333333"
    )
    ax.set_xlabel(titulo_x, fontsize=tam_fonte, fontweight="500", labelpad=10)
    ax.set_ylabel(titulo_y, fontsize=tam_fonte, fontweight="500", labelpad=10)

    ax.tick_params(axis="both", which="major", labelsize=tam_fonte - 2)

    ax.grid(True, linestyle="--", alpha=0.6, which="both")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")

    plt.tight_layout()

    if save == True:
        if titulo == "":
            titulo = f"graph{random.randint(0,100000)}"
        folderData = path("figures")
        folderData.mkdir(parents=True, exist_ok=True)
        plt.savefig(
            f"{folderData}/{titulo.replace(" ", "")}.png", bbox_inches="tight", dpi=300
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
    tam_fonte=12,
    espessura=2,
):  # Função que cria um gráfico de superposição de três curvas distintas com base em um determinado conjunto de parâmetros
    plt.style.use("seaborn-v0_8-muted")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

    ax.plot(
        x1,
        y1,
        linewidth=espessura,
        color="#1a73e8",
        alpha=0.9,
        linestyle="-",
        label=label1,
        solid_capstyle="round",
    )
    ax.plot(
        x2,
        y2,
        linewidth=espessura,
        color="#d93025",
        alpha=0.9,
        linestyle="--",
        label=label2,
        solid_capstyle="round",
    )
    ax.plot(
        x3,
        y3,
        linewidth=espessura,
        color="#1e8e3e",
        alpha=0.9,
        linestyle=":",
        label=label3,
        solid_capstyle="round",
    )

    ax.set_title(
        titulo, fontsize=tam_fonte + 4, fontweight="bold", pad=20, color="#333333"
    )
    ax.set_xlabel(titulo_x, fontsize=tam_fonte, fontweight="500", labelpad=10)
    ax.set_ylabel(titulo_y, fontsize=tam_fonte, fontweight="500", labelpad=10)

    ax.tick_params(axis="both", which="major", labelsize=tam_fonte - 2)
    ax.grid(True, linestyle="--", alpha=0.6, which="both")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")

    ax.legend(fontsize=tam_fonte, frameon=True, shadow=True, loc="best")

    plt.tight_layout()

    if save == True:
        if titulo == "":
            titulo = f"graph{random.randint(0,100000)}"
        plt.savefig(
            f"figures/{titulo.replace(' ','')}.png", bbox_inches="tight", dpi=300
        )

    plt.show()
