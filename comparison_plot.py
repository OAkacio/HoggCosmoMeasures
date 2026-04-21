#
#! -------------------------------------------------- Bibliotecas --------------------------------------------------
from main import *
from src.plot import *
from src.constants import *
from src.parameters import *

#! -------------------------------------------------- Inicia Rotina de Superposição --------------------------------------------------
try:  # * Inicia a rotina principal para 3 universos diferentes
    main(Omega_M, Omega_EE, w, z, z_step, "custom")
    main(1, 0, -1, z, z_step, "M")
    main(0, 1, -1, z, z_step, "EE")
except Exception as e:
    print(f"Um erro foi encontrado ao tentar executar a rotina principal. Erro: {e}")
try:  # * Inicia processo de plotagem dos gráficos de Distância de Luminosidade
    dadosM = "DLdadosM.txt"
    dadosEE = "DLdadosEE.txt"
    dadosMEE = f"DLdados.txt"
    x1 = load_data(f"data/DLdadosM.txt")[0]
    x2 = load_data(f"data/DLdadosEE.txt")[0]
    x3 = load_data(f"data/DLdados.txt")[0]
    y1 = load_data(f"data/DLdadosM.txt")[1]
    y2 = load_data(f"data/DLdadosEE.txt")[1]
    y3 = load_data(f"data/DLdados.txt")[1]
    ppplot(
        True,
        x1,
        y1,
        x2,
        y2,
        x3,
        y3,
        "Universo only-matter",
        "Universo only-lambda",
        "Universo",
        "Comparação de Distâncias de Luminosidade",
        "Redshift (adm.)",
        "Distância de Luminosidade (Mpc)",
    )
except Exception as e:
    print(
        f"Um erro foi encontrado ao tentar fazer a sobreposição dos gráficos de Distância de luminosidade. Erro: {e}"
    )
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
        "Universo only-matter",
        "Universo only-lambda",
        "Universo",
        "Comparação de Módulos e Distância",
        "Redshift (adm.)",
        "Distância de Luminosidade (mag)",
    )
except Exception as e:
    print(
        f"Um erro foi encontrado ao tentar fazer a sobreposição dos gráficos de Módulo de Distância. Erro: {e}"
    )
