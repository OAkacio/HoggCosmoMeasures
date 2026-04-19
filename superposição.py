import numpy as np
from main import *
from src.plot import *


def load_data(caminho_arquivo):
    """
    Lê um arquivo .txt formatado com cabeçalhos '#' e separado por vírgulas.
    Retorna dois vetores (vetor X e vetor Y).
    """
    try:  # Carrega um documento .txt e cria dois vetores para ele no formato ([0=x,[1]=y)
        vetor_x, vetor_y = np.loadtxt(caminho_arquivo, delimiter=",", unpack=True)
        return vetor_x, vetor_y

    except FileNotFoundError:  # Except apra caso o caminho não seja encontrado
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return [], []
    except Exception as e:  # Except para outros casos de falha
        print(f"Erro ao ler o arquivo: {e}")
        return [], []


try:  # Inicia a rotina principal para 3 universos diferentes
    main(0.315, 0.685, -1, 10, 10e-4)
    main(0.2, 0.4, -1, 10, 10e-4)
    main(0.8, 0.6, -1, 10, 10e-4)
except Exception as e:
    print(f"Um erro foi encontrado ao tentar executar a rotina principal. Erro: {e}")

try:  # Inicia processo de plotagem dos gráficos de Distância de Luminosidade
    x1 = load_data("data/DLdadosUniversoAberto.txt")[0]
    x2 = load_data("data/DLdadosUniversoFechado.txt")[0]
    x3 = load_data("data/DLdadosUniversoPlano.txt")[0]

    y1 = load_data("data/DLdadosUniversoAberto.txt")[1]
    y2 = load_data("data/DLdadosUniversoFechado.txt")[1]
    y3 = load_data("data/DLdadosUniversoPlano.txt")[1]

    ppplot(
        True,
        x1,
        y1,
        x2,
        y2,
        x3,
        y3,
        "Universo Aberto",
        "Universo Fechado",
        "Universo Plano",
        "Comparação de Distâncias de Luminosidade",
        "Redshift (adm.)",
        "Distância de Luminosidade (Mpc)",
    )
except Exception as e:
    print(
        f"Um erro foi encontrado ao tentar fazer a sobreposição dos gráficos de Distância de luminosidade. Erro: {e}"
    )

try:
    x1 = load_data("data/MUdadosUniversoAberto.txt")[0]
    x2 = load_data("data/MUdadosUniversoFechado.txt")[0]
    x3 = load_data("data/MUdadosUniversoPlano.txt")[0]

    y1 = load_data("data/MUdadosUniversoAberto.txt")[1]
    y2 = load_data("data/MUdadosUniversoFechado.txt")[1]
    y3 = load_data("data/MUdadosUniversoPlano.txt")[1]

    ppplot(
        True,
        x1,
        y1,
        x2,
        y2,
        x3,
        y3,
        "Universo Aberto",
        "Universo Fechado",
        "Universo Plano",
        "Comparação de Módulos e Distância",
        "Redshift (adm.)",
        "Distância de Luminosidade (mag)",
    )

except Exception as e:
    print(
        f"Um erro foi encontrado ao tentar fazer a sobreposição dos gráficos de Módulo de Distância. Erro: {e}"
    )
