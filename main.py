# -------------------------------------------------- Bibliotecas --------------------------------------------------

import numpy as np
from scipy.integrate import quad

from src.parameters import *
from src.core import *
from src.plot import *
from src.saves import *

# -------------------------------------------------- Início da Rotina --------------------------------------------------


def main():

    print("-" * 100)
    print("\n Inicializando rotina...  \n")
    print("-" * 100)

    try:
        IntANDError = quad(integral, 0, z, args=(Omega_M, Omega_EE))
        resint = IntANDError[0]
        ERRORresint = IntANDError[1]
        print(
            f"Processo de integração numérica finalizado com sucesso!\nResultado da integração: {resint} \nErro estimado: {ERRORresint}"
        )
    except Exception as e:
        print(f"Processo de integração numérica falhou!")

    print("-" * 100)
    print("\n Cálculando dados...  \n")
    print("-" * 100)

    print(f"Parâmetro derivado de curvatura (Omega_K): {Omega_K(Omega_M, Omega_EE)}")
    print(
        f"Tipo de Universo: {UniType(Omega_K(Omega_M,Omega_EE))}, k = {k(Omega_M, Omega_EE)}"
    )
    print(f"Distância comóvel radial (dC): {dC(resint)} Mpc")
    print(f"Parâmetro de desaceleração (q0): {q0(Omega_M, Omega_EE)}")

    print("-" * 100)
    print("\n Iniciando exportação de dados...  \n")
    print("-" * 100)

    try:

        DLvectorX=[]
        DLvectorY=[]
        MUvectorX=[]
        MUvectorY=[]
        DLAPvectorX=[]
        DLAPvectorY=[]

        for i in np.arange(float(z_step),float(z)+float(z_step),float(z_step)):
            resint=quad(integral,0,i,args=(Omega_M,Omega_EE))[0]
            
            DLvectorX.append(i)
            DLvectorY.append(dL(Omega_M,Omega_EE,resint,i))
            
            MUvectorX.append(i)
            MUvectorY.append(mu(Omega_M,Omega_EE,resint,i))
            
            DLAPvectorX.append(i)
            DLAPvectorY.append(approx_dL(Omega_M,Omega_EE,i))

        save_data("DLdados",10,DLvectorX,DLvectorY,"Distribuicao de Distancia de Luminosidade", 0,10,"z","adm.","dL","Mpc")

        save_data("MUdados",10,MUvectorX,MUvectorY,"Distribuicao de Modulo de Distancia", 0,10,"z","adm.","mu","mag")

        save_data("DLAPdados",10,DLAPvectorX,DLAPvectorY,"Distribuicao de Distancia de Luminosidade Aproximada", 0,10,"z","adm.","dL","Mpc")

        print("Exportação de dados concluida com sucesso!")
    except:
        print(f"Falha no processo de salvamento!")

    print("-" * 100)
    print("\n Criando gráficos...  \n")
    print("-" * 100)

    plot(DLvectorX, DLvectorY)
    plot(DLAPvectorX, DLAPvectorY)
    plot(MUvectorX, MUvectorY)


if __name__ == "__main__":
    main()
