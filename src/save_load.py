#
# * =============================================================================
# * DEPENDÊNCIAS
# * =============================================================================

# ? -----------------------------------------------------------------------------
# ?         BIBLIOTECAS
# ? -----------------------------------------------------------------------------

import numpy as np
from pathlib import Path as path


# * =============================================================================
# * FUNÇÕES DE SALVAMENTO
# * =============================================================================


def save_data(
    nome_arquivo="data",
    decimais=10,
    vecX=[],
    vecY=[],
    description="",
    dominio_inferior=0.0,
    dominio_superior=0.0,
    x_grand="",
    x_unit="",
    y_grand="",
    y_unit="",
):
    """Função responsável por salvar um determinado conjunto de dados em um arquivo.txt"""
    data = np.column_stack((vecX, vecY))
    header_text = (
        f"Descripiton: {description}\n"
        f"Domain: {x_grand} in [{dominio_inferior}, {dominio_superior}]\n"
        f"Units: {x_grand} [{x_unit}], {y_grand} [{y_unit}] \n"
        f"{x_grand},{y_grand}"
    )
    folderData = path("data")
    folderData.mkdir(parents=True, exist_ok=True)
    np.savetxt(
        f"{folderData}/{nome_arquivo}.txt",
        data,
        fmt=f"%.{decimais}f",
        delimiter=",",
        header=header_text,
        comments="# ",
    )


# * =============================================================================
# * FUNÇÕES DE CARREGAMENTO
# * =============================================================================


def load_data(caminho_arquivo):
    """
    Lê um arquivo .txt formatado com cabeçalhos '#' e separado por vírgulas.
    Retorna dois vetores (vetor X e vetor Y).
    """
    try:
        vetor_x, vetor_y = np.loadtxt(caminho_arquivo, delimiter=",", unpack=True)
        return vetor_x, vetor_y
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return [], []
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return [], []
    
def load_obs_data(caminho_arquivo):
    """
    Lê um arquivo .txt não formatado e separado por espaços.
    Retorna três vetores (vetor X, vetor Y, vetor Z).
    """
    try:
        vetor_x, vetor_y, vetor_z = np.loadtxt(caminho_arquivo, delimiter=" ", unpack=True)
        return vetor_x, vetor_y, vetor_z
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return [], []
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return [], []