# -------------------------------------------------- Bibliotecas --------------------------------------------------

import numpy as np
from scipy.integrate import quad

from src.parameters import *
from src.core import *
from src.plot import *
from src.save_load import *

# -------------------------------------------------- Início da Rotina --------------------------------------------------


def main(Omega_M, Omega_EE, w, z, z_step):

    print("-" * 100)
    print("\n Inicializando rotina...  \n")
    print("-" * 100)

    try:  # Rotina para realizar a integração numérica e calcular os parâmetros associados
        IntANDError = quad(integral, 0, z, args=(Omega_M, Omega_EE))
        resint = IntANDError[0]
        ERRORresint = IntANDError[1]
        print(
            f"Processo de integração numérica finalizado com sucesso!\nResultado da integração: {resint} \nErro estimado: {ERRORresint}"
        )

    except Exception as e:
        print(f"Processo de integração numérica falhou! Erro: {e}")

    print("-" * 100)
    print("\n Cálculando dados...  \n")
    print("-" * 100)

    print(f"Parâmetro derivado de curvatura (Omega_K): {Omega_K(Omega_M, Omega_EE)}")
    print(
        f"Tipo de Universo: {UniType(Omega_K(Omega_M,Omega_EE))}, k = {k(Omega_M, Omega_EE)}"
    )
    print(f"Distância comóvel radial (dC): {dC(resint)} Mpc")
    print(f"Parâmetro de desaceleração (q0): {q0(Omega_M, Omega_EE,w)}")

    print("-" * 100)
    print("\n Iniciando exportação de dados...  \n")
    print("-" * 100)

    try:  # Rotina para salvar os dados em arquivos .txt e variáveis vetores

        DLvectorX = []
        DLvectorY = []
        MUvectorX = []
        MUvectorY = []
        DLAPvectorX = []
        DLAPvectorY = []
        DIFvectorX = []
        DIFvectorY = []
        iter = 0

        for i in np.arange(float(z_step), float(z) + float(z_step), float(z_step)):
            resint = quad(integral, 0, i, args=(Omega_M, Omega_EE))[0]

            DLvectorX.append(i)
            DLvectorY.append(dL(Omega_M, Omega_EE, resint, i))

            MUvectorX.append(i)
            MUvectorY.append(mu(Omega_M, Omega_EE, resint, i))

            DLAPvectorX.append(i)
            DLAPvectorY.append(approx_dL(Omega_M, Omega_EE, i))

        for y in DLvectorY:
            DIFvectorY.append(y - DLAPvectorY[iter])
            iter = iter + 1
        DIFvectorX = DLvectorX

        save_data(
            f"DLdados OM {Omega_M*100} OEE {Omega_EE*100}",
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
            f"MUdados OM {Omega_M*100} OEE {Omega_EE*100}",
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
            f"DLAPdados OM {Omega_M*100} OEE {Omega_EE*100}",
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
            f"DIFdados OM {Omega_M*100} OEE {Omega_EE*100}",
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

        print("Exportação de dados concluida com sucesso!")

    except Exception as e:
        print(f"Falha no processo de salvamento! Erro: {e}")

    print("-" * 100)
    print("\n Criando gráficos...  \n")
    print("-" * 100)

    try:  # Rotina para plotagem dos gráficos
        plot(
            True,
            DLvectorX,
            DLvectorY,
            f"Distância de Luminosidade Exata OM {Omega_M*100} OEE {Omega_EE*100}",
            "Redshift (adm.)",
            "Distância de Luminosidade (Mpc)",
        )
        plot(
            True,
            DLAPvectorX,
            DLAPvectorY,
            f"Distância de Luminosidade Aproximada OM {Omega_M*100} OEE {Omega_EE*100}",
            "Redshift (adm.)",
            "Distância de Luminosidade (Mpc)",
        )
        plot(
            True,
            DIFvectorX,
            DIFvectorY,
            f"Anlálise de Erro Aproximação vs. Exato OM {Omega_M*100} OEE {Omega_EE*100}",
            "Redshift (adm.)",
            "dL Exato - dL Aproximado  (Mpc)",
        )
        plot(
            True,
            MUvectorX,
            MUvectorY,
            f"Módulo de Distância Exato OM {Omega_M*100} OEE {Omega_EE*100}",
            "Redshift (adm.)",
            "Módulo de Distância (mag)",
        )

    except Exception as e:
        print(f"Falha no processo de plotagem dos gráficos! Erro: {e}")

def superposicao(Omega_M, Omega_EE, w, z, z_step):

    try:  # Inicia a rotina principal para 3 universos diferentes
        main(Omega_M, Omega_EE, w, z, z_step)
        main(1, 0, w, z, z_step)
        main(0, 1, w, z, z_step)

    except Exception as e:
        print(f"Um erro foi encontrado ao tentar executar a rotina principal. Erro: {e}")

    try:  # Inicia processo de plotagem dos gráficos de Distância de Luminosidade
        dadosM = "DLdados OM 100 OEE 0.txt"
        dadosEE = "DLdados OM 0 OEE 100.txt"
        dadosMEE = f"DLdados OM {Omega_M*100} OEE {Omega_EE*100}.txt"

        x1 = load_data(f"data/{dadosM}")[0]
        x2 = load_data(f"data/{dadosEE}")[0]
        x3 = load_data(f"data/{dadosMEE}")[0]

        y1 = load_data(f"data/{dadosM}")[1]
        y2 = load_data(f"data/{dadosEE}")[1]
        y3 = load_data(f"data/{dadosMEE}")[1]

        ppplot(
            True,
            x1,
            y1,
            x2,
            y2,
            x3,
            y3,
            "Universo OM",
            "Universo OEE",
            "Universo OMEE",
            "Comparação de Distâncias de Luminosidade",
            "Redshift (adm.)",
            "Distância de Luminosidade (Mpc)",
        )
    except Exception as e:
        print(
            f"Um erro foi encontrado ao tentar fazer a sobreposição dos gráficos de Distância de luminosidade. Erro: {e}"
        )

    try:

        dadosM = "MUdados OM 100 OEE 0.txt"
        dadosEE = "MUdados OM 0 OEE 100.txt"
        dadosMEE = f"MUdados OM {Omega_M*100} OEE {Omega_EE*100}.txt"

        x1 = load_data(f"data/{dadosM}")[0]
        x2 = load_data(f"data/{dadosEE}")[0]
        x3 = load_data(f"data/{dadosMEE}")[0]

        y1 = load_data(f"data/{dadosM}")[1]
        y2 = load_data(f"data/{dadosEE}")[1]
        y3 = load_data(f"data/{dadosMEE}")[1]

        ppplot(
            True,
            x1,
            y1,
            x2,
            y2,
            x3,
            y3,
            "Universo OM",
            "Universo OEE",
            "Universo OMEE",
            "Comparação de Módulos e Distância",
            "Redshift (adm.)",
            "Distância de Luminosidade (mag)",
        )

    except Exception as e:
        print(
            f"Um erro foi encontrado ao tentar fazer a sobreposição dos gráficos de Módulo de Distância. Erro: {e}"
        )


if __name__ == "__main__":
    superposicao(Omega_M, Omega_EE, w, z, z_step)
