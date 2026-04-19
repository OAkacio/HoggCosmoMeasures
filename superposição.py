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
    main(1, 0, -1, 10, 10e-4)
    main(0, 1, -1, 10, 10e-4)
except Exception as e:
    print(f"Um erro foi encontrado ao tentar executar a rotina principal. Erro: {e}")

try:  # Inicia processo de plotagem dos gráficos de Distância de Luminosidade
    dadosM = "DLdados OM 100 OEE 0.txt"
    dadosEE = "DLdados OM 0 OEE 100.txt"
    dadosMEE = "DLdados OM 31.5 OEE 68.5.txt"

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
    dadosMEE = "MUdados OM 31.5 OEE 68.5.txt"

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
