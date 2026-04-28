#
# * =============================================================================
# * DEPENDÊNCIAS
# * =============================================================================

# ? -----------------------------------------------------------------------------
# ?         BIBLIOTECAS
# ? -----------------------------------------------------------------------------

import numpy as np

# ? -----------------------------------------------------------------------------
# ?         MÓDULOS LOCAIS
# ? -----------------------------------------------------------------------------

from src.constants import *
from toolkit import graphs as gp
from toolkit import system as sy
from toolkit import saveload as sl

# * =============================================================================
# * ROTINA PRINCIPAL
# * =============================================================================

sy.header("Análise de Universo Simulado", Folder="/data/...")

# ? -----------------------------------------------------------------------------
# ?         CARREGANDO DADOS DO UNIVERSO SIMULADO
# ? -----------------------------------------------------------------------------

try:
    sy.status("Iniciando carregamento de dados...")
    DLvectorX = sl.loadtable(f"data/DLdados.txt")[0]
    DLAPvectorX = sl.loadtable(f"data/DLAPdados.txt")[0]
    DIFvectorX = sl.loadtable(f"data/DIFdados.txt")[0]
    MUvectorX = sl.loadtable(f"data/MUdados.txt")[0]
    DLvectorY = sl.loadtable(f"data/DLdados.txt")[1]
    DLAPvectorY = sl.loadtable(f"data/DLAPdados.txt")[1]
    DIFvectorY = sl.loadtable(f"data/DIFdados.txt")[1]
    MUvectorY = sl.loadtable(f"data/MUdados.txt")[1]
    infos = sl.loadtable(f"data/infos.txt")[0]
    sy.ok(("infos", "DLdados", "MUdados", "DLAPdados", "DIFdados"))
    sy.status("Dados carregados com sucesso!")
    sy.param(
        ("Omega_M", infos[0]), ("Omega_EE", infos[1]), ("w", infos[2]), ("z", infos[3])
    )

    # ? -----------------------------------------------------------------------------
    # ?         GERANDO GRÁFICOS DE PARÂMETROS
    # ? -----------------------------------------------------------------------------

    sy.status("Iniciando criação do gráficos...")
    gp.basic(
        DLvectorX,
        DLvectorY / (c / H0),
        "",
        r"$z$",
        r"$d_L \; /\; \left(\frac{c}{H_0}\right)$",
        save=True,
        nome="DLdistribuicao",
    )
    gp.multi(
        (
            DLvectorX,
            DLAPvectorX,
        ),
        (DLvectorY / (c / H0), DLAPvectorY / (c / H0)),
        titulo="",
        NOMEvecx=r"$z$",
        NOMEvecy=r"$d_L \; /\; \left(\frac{c}{H_0}\right)$",
        nomes_curvas=("Curva Exata", "Curva Aproximada"),
        save=True,
        nome="ExataAproximadadistribuicao",
    )
    gp.multi(
        (DIFvectorX, DIFvectorX),
        (DIFvectorY, np.full(len(DIFvectorY), 0)),
        titulo="",
        NOMEvecx=r"$z$",
        NOMEvecy=r"$d_L \; /\; \left(\frac{c}{H_0}\right)$",
        nomes_curvas=("Diferença Exato vs. Aproximado", "Zero"),
        save=True,
        nome="DIFdistribuicao",
    )
    gp.basic(MUvectorX, MUvectorY, "", r"$z$", r"$\mu$ (mag)", save=True, nome="MUdistribuicao")
    sy.ok(
        (
            "Gráfico de Distância de Luminosidade",
            "Gráfico de Distância de Luminosidade Aproximada",
            "Gráfico de Anlálise de Erro Aproximação vs. Exato",
            "Gráfico de Módulo de Distância",
        )
    )
    sy.fim()
except Exception as e:
    sy.status(f"Falha no processo de plotagem dos gráficos! Erro: {e}")
