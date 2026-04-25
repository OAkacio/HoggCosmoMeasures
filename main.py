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

from src.parameters import *
from src.core import *
from src.save_load import *
from src.constants import *
from src.system import *


# * =============================================================================
# * ROTINA PRINCIPAL
# * =============================================================================

# ? -----------------------------------------------------------------------------
# ?         FUNÇÃO MAIN
# ? -----------------------------------------------------------------------------


def main(Omega_M, Omega_EE, w, z, z_step, type="custom"):
    header(
        "iniciando HoggCosmoMeasures...", Omega_M=Omega_M, Omega_EE=Omega_EE, w=w, z=z
    )
    try:
        resintlist = integracao(integral, Omega_M, Omega_EE, z)
        status("Processo de integração numérica finalizado com sucesso!")
        param("Integração Numérica", resintlist[0], "Mpc")
        param("Erro Estimado", resintlist[1], "Mpc")
        param(
            "Distância de Luminosidade para 'z' (dL(z))",
            dL(Omega_M, Omega_EE, resintlist[0], z),
            "Mpc",
        )
        param(
            "Módulo de Distância para 'z' (mu(z))",
            mu(Omega_M, Omega_EE, resintlist[0], z),
            "mag",
        )
    except Exception as e:
        status(f"Processo de integração numérica falhou! Erro: {e}")
    status("Iniciando cálculo de parâmetros do universo")
    param("Tipo de universo", UniType(Omega_K(Omega_M, Omega_EE)))
    param("Constante de curvatura espacial (k)", k(Omega_M, Omega_EE))
    param("Parâmetro derivado de curvatura (Omega_K)", Omega_K(Omega_M, Omega_EE))
    param("Distância comóvel radial (dC)", dC(resintlist[0]), "Mpc")
    param("Parâmetro de desaceleração (q0)", q0(Omega_M, Omega_EE, w))
    status("Iniciando exportação de dados")
    try:
        sollist = solution(Omega_M, Omega_EE, z, z_step)
        DLvectorX = sollist[0]
        DLvectorY = sollist[1]
        MUvectorX = sollist[2]
        MUvectorY = sollist[3]
        DLAPvectorX = sollist[4]
        DLAPvectorY = sollist[5]
        DIFvectorX = sollist[6]
        DIFvectorY = sollist[7]
        if type == "custom":
            save_data(
                f"DLdados",
                10,
                DLvectorX,
                DLvectorY,
                "Distribuicao de Distancia de Luminosidade",
                0,
                10,
                "z",
                "adm.",
                "dL",
                "Mpc",
            )
            save_data(
                f"MUdados",
                10,
                MUvectorX,
                MUvectorY,
                "Distribuicao de Modulo de Distancia",
                0,
                10,
                "z",
                "adm.",
                "mu",
                "mag",
            )
            save_data(
                f"DLAPdados",
                10,
                DLAPvectorX,
                DLAPvectorY,
                "Distribuicao de Distancia de Luminosidade Aproximada",
                0,
                10,
                "z",
                "adm.",
                "dL",
                "Mpc",
            )
            save_data(
                f"DIFdados",
                10,
                DIFvectorX,
                DIFvectorY,
                "Analise de Erro na Distribuicao de Distancia de Luminosidade exata e Aproximada",
                0,
                10,
                "z",
                "adm.",
                "dL",
                "Mpc",
            )
        elif type == "M":
            save_data(
                f"DLdadosM",
                10,
                DLvectorX,
                DLvectorY,
                "Distribuicao de Distancia de Luminosidade",
                0,
                10,
                "z",
                "adm.",
                "dL",
                "Mpc",
            )
            save_data(
                f"MUdadosM",
                10,
                MUvectorX,
                MUvectorY,
                "Distribuicao de Modulo de Distancia",
                0,
                10,
                "z",
                "adm.",
                "mu",
                "mag",
            )
            save_data(
                f"DLAPdadosM",
                10,
                DLAPvectorX,
                DLAPvectorY,
                "Distribuicao de Distancia de Luminosidade Aproximada",
                0,
                10,
                "z",
                "adm.",
                "dL",
                "Mpc",
            )
            save_data(
                f"DIFdadosM",
                10,
                DIFvectorX,
                DIFvectorY,
                "Analise de Erro na Distribuicao de Distancia de Luminosidade exata e Aproximada",
                0,
                10,
                "z",
                "adm.",
                "dL",
                "Mpc",
            )
        elif type == "EE":
            save_data(
                f"DLdadosEE",
                10,
                DLvectorX,
                DLvectorY,
                "Distribuicao de Distancia de Luminosidade",
                0,
                10,
                "z",
                "adm.",
                "dL",
                "Mpc",
            )
            save_data(
                f"MUdadosEE",
                10,
                MUvectorX,
                MUvectorY,
                "Distribuicao de Modulo de Distancia",
                0,
                10,
                "z",
                "adm.",
                "mu",
                "mag",
            )
            save_data(
                f"DLAPdadosEE",
                10,
                DLAPvectorX,
                DLAPvectorY,
                "Distribuicao de Distancia de Luminosidade Aproximada",
                0,
                10,
                "z",
                "adm.",
                "dL",
                "Mpc",
            )
            save_data(
                f"DIFdadosEE",
                10,
                DIFvectorX,
                DIFvectorY,
                "Analise de Erro na Distribuicao de Distancia de Luminosidade exata e Aproximada",
                0,
                10,
                "z",
                "adm.",
                "dL",
                "Mpc",
            )
        status("Exportação de dados concluida com sucesso!")
        status("Rotina principal finalizada!")
    except Exception as e:
        status(f"Falha no processo de salvamento! Erro: {e}")
    return None


# ? -----------------------------------------------------------------------------
# ?         MAIN GUARD
# ? -----------------------------------------------------------------------------


if __name__ == "__main__":
    main(Omega_M, Omega_EE, w, z, z_step, type="custom")
