#
# * =============================================================================
# * DEPENDÊNCIAS
# * =============================================================================

# ? -----------------------------------------------------------------------------
# ?         MÓDULOS LOCAIS
# ? -----------------------------------------------------------------------------

from src.plot import *
from src.save_load import *
from src.system import *
from src.constants import *

# * =============================================================================
# * ROTINA PRINCIPAL
# * =============================================================================

header("Iniciando basic plots...")

try:
    DLvectorX = load_data(f"data/DLdados.txt")[0]
    DLAPvectorX = load_data(f"data/DLAPdados.txt")[0]
    DIFvectorX = load_data(f"data/DIFdados.txt")[0]
    MUvectorX = load_data(f"data/MUdados.txt")[0]
    DLvectorY = load_data(f"data/DLdados.txt")[1]
    DLAPvectorY = load_data(f"data/DLAPdados.txt")[1]
    DIFvectorY = load_data(f"data/DIFdados.txt")[1]
    MUvectorY = load_data(f"data/MUdados.txt")[1]
    plot(
        True,
        DLvectorX,
        DLvectorY / (c / H0),
        f"Curva de Distância de Luminosidade",
        "z",
        r"$d_L \; /\; \left(\frac{c}{H_0}\right)$",
    )
    plot(
        True,
        DLAPvectorX,
        DLAPvectorY / (c / H0),
        f"Curva de Distância de Luminosidade Aproximada",
        "z",
        r"$d_L \; /\; \left(\frac{c}{H_0}\right)$",
    )
    plot(
        True,
        DIFvectorX,
        DIFvectorY / (c / H0),
        f"Anlálise de Erro Aproximação vs. Exato",
        "z",
        r"$d_L \; /\; \left(\frac{c}{H_0}\right)$",
    )
    plot(
        True,
        MUvectorX,
        MUvectorY,
        f"Curva de Módulo de Distância",
        "z",
        r"$\mu$ (mag)",
    )
    status("Criação e salvamento dos gráficos concluida com sucesso!")
    status("Rotina de criação de gráficos finalizada")
except Exception as e:
    status(f"Falha no processo de plotagem dos gráficos! Erro: {e}")
