#
# * =============================================================================
# * DEPENDÊNCIAS
# * =============================================================================

# ? -----------------------------------------------------------------------------
# ?         MÓDULOS LOCAIS
# ? -----------------------------------------------------------------------------

from main import *
from src.constants import *
from src.parameters import *
from toolkit import graphs as gp
from toolkit import system as sy
from toolkit import saveload as sl


# * =============================================================================
# * ROTINA PRINCIPAL
# * =============================================================================

# ? -----------------------------------------------------------------------------
# ?         GERANDO DADOS DOS UNIVERSOS ANALISADOS
# ? -----------------------------------------------------------------------------

try:
    sy.header("Comparação de Universos", Folder="/data/...")
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
    sy.status("Iniciando análise de universo de somente materia...")
    main(1, 0, -1, z, "M")
    sy.status("Iniciando análise de universo de somente energia...")
    main(0, 1, -1, z, "EE")
except Exception as e:
    sy.status(
        f"Um erro foi encontrado ao tentar executar a rotina principal. Erro: {e}"
    )

# ? -----------------------------------------------------------------------------
# ?         GERANDO GRÁFICOS PARA DISTÂNCIA DE LUMINOSIDADE
# ? -----------------------------------------------------------------------------

try:
    sy.status("Carregando dados gerados....")
    dadosM = "DLdadosM.txt"
    dadosEE = "DLdadosEE.txt"
    dadosMEE = f"DLdados.txt"
    x1 = sl.loadtable(f"data/DLdadosM.txt")[0]
    x2 = sl.loadtable(f"data/DLdadosEE.txt")[0]
    x3 = sl.loadtable(f"data/DLdados.txt")[0]
    y1 = sl.loadtable(f"data/DLdadosM.txt")[1] / (c / H0)
    y2 = sl.loadtable(f"data/DLdadosEE.txt")[1] / (c / H0)
    y3 = sl.loadtable(f"data/DLdados.txt")[1] / (c / H0)
    sy.ok(("DLdados", "DLdadosM", "DLdadosEE"))
    sy.status("Iniciando geração de gráficos...")
    gp.multi(
        (x1, x2, x3),
        (y1, y2, y3),
        titulo="",
        NOMEvecx=r"$z$",
        NOMEvecy=r"$d_L \; /\; \left(\frac{c}{H_0}\right)$",
        nomes_curvas=(
            r"Somente Matéria $(\Omega_m=1.0, \Omega_\Lambda=0.0)$",
            r"Somente Energia $(\Omega_m=0.0, \Omega_\Lambda=1.0)$",
            rf"Universo Simulado $(\Omega_m={Omega_M}, \Omega_\Lambda={Omega_EE})$",
        ),
        save=True,
        nome="DLComparacao",
    )
except Exception as e:
    sy.status(
        f"Um erro foi encontrado ao tentar fazer a sobreposição dos gráficos de Distância de luminosidade. Erro: {e}"
    )

# ? -----------------------------------------------------------------------------
# ?         GERANDO GRÁFICOS PARA MÓDULO DE DISTÂNCIA
# ? -----------------------------------------------------------------------------

try:
    dadosM = "MUdadosM.txt"
    dadosEE = "MUdadosEE.txt"
    dadosMEE = f"MUdados.txt"
    x1 = sl.loadtable(f"data/MUdadosM.txt")[0]
    x2 = sl.loadtable(f"data/MUdadosEE.txt")[0]
    x3 = sl.loadtable(f"data/MUdados.txt")[0]
    y1 = sl.loadtable(f"data/MUdadosM.txt")[1]
    y2 = sl.loadtable(f"data/MUdadosEE.txt")[1]
    y3 = sl.loadtable(f"data/MUdados.txt")[1]
    gp.multi(
        (x1, x2, x3),
        (y1, y2, y3),
        titulo="",
        nomes_curvas=(
            r"Somente Matéria $(\Omega_m=1.0, \Omega_\Lambda=0.0)$",
            r"Somente Energia $(\Omega_m=0.0, \Omega_\Lambda=1.0)$",
            rf"Universo Simulado $(\Omega_m={Omega_M}, \Omega_\Lambda={Omega_EE})$",
        ),
        NOMEvecx=r"$z$",
        NOMEvecy=r"$\mu$ (mag)",
        save=True,
        nome="MUcomparacao",
    )
except Exception as e:
    sy.status(
        f"Um erro foi encontrado ao tentar fazer a sobreposição dos gráficos de Módulo de Distância. Erro: {e}"
    )
try:
    dadosM = "DLAPdadosM.txt"
    dadosEE = "DLAPdadosEE.txt"
    dadosMEE = "DLAPdados.txt"
    x1 = sl.loadtable(f"data/DLAPdadosM.txt")[0]
    x2 = sl.loadtable(f"data/DLAPdadosEE.txt")[0]
    x3 = sl.loadtable(f"data/DLAPdados.txt")[0]
    y1 = sl.loadtable(f"data/DLAPdadosM.txt")[1]/ (c / H0)
    y2 = sl.loadtable(f"data/DLAPdadosEE.txt")[1]/ (c / H0)
    y3 = sl.loadtable(f"data/DLAPdados.txt")[1]/ (c / H0)
    gp.multi(
        (x1, x2, x3),
        (y1, y2, y3),
        titulo="",
        nomes_curvas=(
            r"Somente Matéria $(\Omega_m=1.0, \Omega_\Lambda=0.0)$",
            r"Somente Energia $(\Omega_m=0.0, \Omega_\Lambda=1.0)$",
            rf"Universo Simulado $(\Omega_m={Omega_M}, \Omega_\Lambda={Omega_EE})$",
        ),
        NOMEvecx=r"$z$",
        NOMEvecy=r"$d_L \; /\; \left(\frac{c}{H_0}\right)$",
        save=True,
        nome="DLAPcomparacao"
    )
except:
    sy.status(
        f"Um erro foi encontrado ao tentar fazer a sobreposição dos gráficos de Distância de luminosidade Aproximada. Erro: {e}"
    )
sy.ok(
    (
        "Gráfico de Distância de Luminosidade Exata dos Universos",
        "Gráfico de Módulo de Distância dos Universos",
        "Gráfico de Distância de Luminosidade Aproxiomada dos Universos",
    )
)

sy.fim()
