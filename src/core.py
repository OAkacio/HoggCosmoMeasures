#-------------------------------------------------- Bibliotecas --------------------------------------------------

import numpy as np

from src.parameters import *

#-------------------------------------------------- Funções Fundamentais --------------------------------------------------

def q0(Omega_M, Omega_EE):
    """Calcula o parâmetro de desaceleração atual (q0) a partir dos parâmetros de densidade de matéria e energia escura."""
    return 0.5 * Omega_M - Omega_EE

def dL(dm, z):
    """Calcula a distância de luminosidade (dL) a partir da distância comóvel transversal (dm) e do redshift (z)."""
    return (1 + z) * dm

def approx_dL(Omega_M, Omega_EE, z):
    """Calcula a aproximação de distância de luminosidade (dL) para pequenos redshifts (z) usando o parâmetro de desaceleração (q0)."""
    return (c/H0)*z*(1 + (1 - q0(Omega_M, Omega_EE))*z/2)

def Omega_K(Omega_M, Omega_EE):
    """Calcula o parâmetro de curvatura (Omega_K) a partir dos parâmetros de densidade de matéria e energia escura."""
    return 1 - (Omega_M + Omega_EE)

def mu(dm, z):
    """Calcula a magnitude de distância (mu) a partir da distância de luminosidade (dL) e do redshift (z)."""
    return 5 * np.log10(dL(dm,z)) + 25

def E(z, Omega_M, Omega_EE):
    """Calcula a função de expansão (E) a partir do redshift (z) e dos parâmetros de densidade de matéria e energia escura."""
    return np.sqrt(Omega_M * (1 + z)**3 + Omega_EE*(1+z)**3*(1+w)+ Omega_K(Omega_M, Omega_EE) * (1 + z)**2)

def Sk(k,r):
    """Calcula a função de distância comóvel transversal (Sk) a partir do parâmetro de curvatura (k) e da distância comóvel radial (r)."""
    if k > 0:
        return np.sin(np.sqrt(k)*r)/np.sqrt(k)
    elif k < 0:
        return np.sinh(np.sqrt(-k)*r)/np.sqrt(-k)
    else:
        return r
    
def dm(k,dC):
    """Calcula a distância comóvel transversal (dm) a partir do parâmetro de curvatura (k) e da distância comóvel radial (dC)."""
    return Sk(k,dC)

#...