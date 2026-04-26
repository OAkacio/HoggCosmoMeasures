#
# * =============================================================================
# * DEPENDÊNCIAS
# * =============================================================================

# ? -----------------------------------------------------------------------------
# ?         MÓDULOS LOCAIS
# ? -----------------------------------------------------------------------------

from main import *
from src.plot import *
from src.constants import *
from src.parameters import *
from src.system import *

# * =============================================================================
# * ROTINA PRINCIPAL
# * =============================================================================

# ? -----------------------------------------------------------------------------
# ?         GERANDO DADOS DOS UNIVERSOS ANALISADOS
# ? -----------------------------------------------------------------------------

try:
    header("Iniciando comparison plot...", Folder="/data/...")
    space()
    status("Iniciando 1a análise")
    main(Omega_M, Omega_EE, w, z, z_step, "custom")
    space()
    status("Iniciando 2a análise")
    main(1, 0, -1, z, z_step, "M")
    space()
    status("Iniciando 3a análise")
    main(0, 1, -1, z, z_step, "EE")
    space()
except Exception as e:
    status(f"Um erro foi encontrado ao tentar executar a rotina principal. Erro: {e}")

# ? -----------------------------------------------------------------------------
# ?         GERANDO GRÁFICOS PARA DISTÂNCIA DE LUMINOSIDADE
# ? -----------------------------------------------------------------------------

try:
    status("Iniciando criação de gráficos")
    dadosM = "DLdadosM.txt"
    dadosEE = "DLdadosEE.txt"
    dadosMEE = f"DLdados.txt"
    x1 = load_data(f"data/DLdadosM.txt")[0]
    x2 = load_data(f"data/DLdadosEE.txt")[0]
    x3 = load_data(f"data/DLdados.txt")[0]
    y1 = load_data(f"data/DLdadosM.txt")[1] / (c / H0)
    y2 = load_data(f"data/DLdadosEE.txt")[1] / (c / H0)
    y3 = load_data(f"data/DLdados.txt")[1] / (c / H0)
    ppplot(
        True,
        x1,
        y1,
        x2,
        y2,
        x3,
        y3,
        r"Matter-only $(\Omega_m=1.0, \Omega_\Lambda=0.0)$",
        r"$\Lambda$-only $(\Omega_m=0.0, \Omega_\Lambda=1.0)$",
        rf"Universo Simulado $(\Omega_m={Omega_M}, \Omega_\Lambda={Omega_EE})$",
        "Comparação de Distâncias de Luminosidade",
        "z",
        r"$d_L \; /\; \left(\frac{c}{H_0}\right)$",
        espessura=2.5,
    )
except Exception as e:
    status(
        f"Um erro foi encontrado ao tentar fazer a sobreposição dos gráficos de Distância de luminosidade. Erro: {e}"
    )

# ? -----------------------------------------------------------------------------
# ?         GERANDO GRÁFICOS PARA MÓDULO DE DISTÂNCIA
# ? -----------------------------------------------------------------------------

try:
    dadosM = "MUdadosM.txt"
    dadosEE = "MUdadosEE.txt"
    dadosMEE = f"MUdados.txt"
    x1 = load_data(f"data/MUdadosM.txt")[0]
    x2 = load_data(f"data/MUdadosEE.txt")[0]
    x3 = load_data(f"data/MUdados.txt")[0]
    y1 = load_data(f"data/MUdadosM.txt")[1]
    y2 = load_data(f"data/MUdadosEE.txt")[1]
    y3 = load_data(f"data/MUdados.txt")[1]
    ppplot(
        True,
        x1,
        y1,
        x2,
        y2,
        x3,
        y3,
        r"Matter-only $(\Omega_m=1.0, \Omega_\Lambda=0.0)$",
        r"$\Lambda$-only $(\Omega_m=0.0, \Omega_\Lambda=1.0)$",
        rf"Universo Simulado $(\Omega_m={Omega_M}, \Omega_\Lambda={Omega_EE})$",
        "Comparação de Módulos e Distância",
        "z",
        r"$\mu$ (mag)",
    )
except Exception as e:
    status(
        f"Um erro foi encontrado ao tentar fazer a sobreposição dos gráficos de Módulo de Distância. Erro: {e}"
    )
try:
    dadosM = "DLAPdadosM.txt"
    dadosEE = "DLAPdadosEE.txt"
    dadosMEE = "DLAPdados.txt"
    x1 = load_data(f"data/DLAPdadosM.txt")[0]
    x2 = load_data(f"data/DLAPdadosEE.txt")[0]
    x3 = load_data(f"data/DLAPdados.txt")[0]
    y1 = load_data(f"data/DLAPdadosM.txt")[1]
    y2 = load_data(f"data/DLAPdadosEE.txt")[1]
    y3 = load_data(f"data/DLAPdados.txt")[1]
    ppplot(
        True,
        x1,
        y1,
        x2,
        y2,
        x3,
        y3,
        r"Matter-only $(\Omega_m=1.0, \Omega_\Lambda=0.0)$",
        r"$\Lambda$-only $(\Omega_m=0.0, \Omega_\Lambda=1.0)$",
        rf"Universo Simulado $(\Omega_m={Omega_M}, \Omega_\Lambda={Omega_EE})$",
        "Comparação de Distâncias de Luminosidade Aproximada",
        "z",
        r"$\mu$ (mag)",
    )
except:
    status(
        f"Um erro foi encontrado ao tentar fazer a sobreposição dos gráficos de Distância de luminosidade Aproximada. Erro: {e}"
    )

status("EXECUÇÃO FINALIZADA!")
