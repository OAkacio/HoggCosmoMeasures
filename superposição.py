import numpy as np
from main import *
from src.plot import *

def load_data(caminho_arquivo):
    """
    Lê um arquivo .txt formatado com cabeçalhos '#' e separado por vírgulas.
    Retorna dois arrays (vetor X e vetor Y).
    """
    try:
        # O argumento unpack=True transpõe a matriz automaticamente, 
        # separando a coluna 0 para o X e a coluna 1 para o Y.
        vetor_x, vetor_y = np.loadtxt(caminho_arquivo, delimiter=',', unpack=True)
        return vetor_x, vetor_y
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return [], []
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return [], []
    
main(0.315,0.685,-1,10,10e-4)
main(0.2,0.4,-1,10,10e-4)
main(0.8,0.6,-1,10,10e-4)

x1=load_data("data/DLdadosUniversoAberto.txt")[0]
x2=load_data("data/DLdadosUniversoFechado.txt")[0]
x3=load_data("data/DLdadosUniversoPlano.txt")[0]

y1=load_data("data/DLdadosUniversoAberto.txt")[1]
y2=load_data("data/DLdadosUniversoFechado.txt")[1]
y3=load_data("data/DLdadosUniversoPlano.txt")[1]

ppplot(True,x1, y1,x2,y2,x3,y3, "Comparação Distância de Luminosidade","Redshift (adm.)", "Distância de Luminosidade (Mpc)")