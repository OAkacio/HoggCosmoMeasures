#
#! -------------------------------------------------- Bibliotecas --------------------------------------------------
from src.plot import *
from src.save_load import *

#! -------------------------------------------------- Lendo, Criando e Salvando Gráficos --------------------------------------------------
print("-" * 100)
print("\n Criando gráficos...  \n")
print("-" * 100)
try:  # * Rotina para plotagem dos gráficos
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
        DLvectorY,
        f"Curva de Distância de Luminosidade",
        "Redshift (adm.)",
        "Distância de Luminosidade (Mpc)",
    )
    plot(
        True,
        DLAPvectorX,
        DLAPvectorY,
        f"Curva de Distância de Luminosidade Aproximada",
        "Redshift (adm.)",
        "Distância de Luminosidade (Mpc)",
    )
    plot(
        True,
        DIFvectorX,
        DIFvectorY,
        f"Anlálise de Erro Aproximação vs. Exato",
        "Redshift (adm.)",
        "dL Exato - dL Aproximado  (Mpc)",
    )
    plot(
        True,
        MUvectorX,
        MUvectorY,
        f"Curva de Módulo de Distância",
        "Redshift (adm.)",
        "Módulo de Distância (mag)",
    )
    print("Criação e salvamento dos gráficos concluida com sucesso!")
except Exception as e:
    print(f"Falha no processo de plotagem dos gráficos! Erro: {e}")
