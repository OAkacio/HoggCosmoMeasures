#
# * =============================================================================
# * DEPENDÊNCIAS
# * =============================================================================

# ? -----------------------------------------------------------------------------
# ?         BIBLIOTECAS
# ? -----------------------------------------------------------------------------

import numpy as np
from scipy.integrate import quad
from tqdm import tqdm

# ? -----------------------------------------------------------------------------
# ?         MÓDULOS LOCAIS
# ? -----------------------------------------------------------------------------

from src.parameters import *


# * =============================================================================
# * FUNÇÕES MATEMÁTICAS
# * =============================================================================

# ? -----------------------------------------------------------------------------
# ?         FUNÇÕES FÍSICAS
# ? -----------------------------------------------------------------------------


def q0(Omega_M, Omega_EE, w):
    """Calcula o parâmetro de desaceleração atual (q0) a partir dos parâmetros de densidade de matéria e energia escura."""
    return 0.5 * Omega_M + 0.5 * Omega_EE * (1 + 3 * w)


def dL(Omega_M, Omega_EE, resint, z):
    """Calcula a distância de luminosidade (dL) a partir da distância comóvel transversal (dm) e do redshift (z)."""
    return (1 + z) * dm(Omega_M, Omega_EE, resint)


def approx_dL(Omega_M, Omega_EE, z):
    """Calcula a aproximação de distância de luminosidade (dL) para pequenos redshifts (z) usando o parâmetro de desaceleração (q0)."""
    return (c / H0) * z * (1 + (1 - q0(Omega_M, Omega_EE, w)) * z / 2)


def Omega_K(Omega_M, Omega_EE):
    """Calcula o parâmetro de curvatura (Omega_K) a partir dos parâmetros de densidade de matéria e energia escura."""
    return 1 - (Omega_M + Omega_EE)


def mu(Omega_M, Omega_EE, resint, z):
    """Calcula a magnitude de distância (mu) a partir da distância de luminosidade (dL) e do redshift (z)."""
    return 5 * np.log10(dL(Omega_M, Omega_EE, resint, z)) + 25


def E(z, Omega_M, Omega_EE):
    """Calcula a função de expansão (E) a partir do redshift (z) e dos parâmetros de densidade de matéria e energia escura."""
    return np.sqrt(
        Omega_M * (1 + z) ** 3
        + Omega_EE * (1 + z) ** (3 * (1 + w))
        + Omega_K(Omega_M, Omega_EE) * (1 + z) ** 2
    )


def Sk(Omega_M, Omega_EE, r):
    """Calcula a função de distância comóvel transversal (Sk) a partir do parâmetro de curvatura (k) e da distância comóvel radial (r)."""
    Ok = Omega_K(Omega_M, Omega_EE)
    DH = c / H0
    if Ok > 0:
        return (DH / np.sqrt(Ok)) * np.sinh(np.sqrt(Ok) * r / DH)
    elif Ok < 0:
        return (DH / np.sqrt(-Ok)) * np.sin(np.sqrt(-Ok) * r / DH)
    else:
        return r


def dm(Omega_M, Omega_EE, resint):
    """Calcula a distância comóvel transversal (dm) a partir do parâmetro de curvatura (k) e da distância comóvel radial (dC)."""
    return Sk(Omega_M, Omega_EE, dC(resint))


def dC(resint):
    """Calcula o valor de distância comóvel radial (dC) a partir do resultado da integração dda função integral."""
    return (c / H0) * resint


def k(Omega_M, Omega_EE):
    """Determina o parâmetro de curvatura com base no valor do Parâmetro de Densidade de Curvatura (Omega_k)"""
    Ok = Omega_K(Omega_M, Omega_EE)
    if Ok > 0:
        return -1
    elif Ok < 0:
        return +1
    else:
        return 0


# ? -----------------------------------------------------------------------------
# ?         FUNÇÕES SISTEMÁTICAS DE CÁLCULO NO MAIN
# ? -----------------------------------------------------------------------------


def integral(z, Omega_M, Omega_EE):
    """Formaliza a quantidade a ser integrada para o cálculo da distância comóvel radial (dC) a partir do redshift (z) e dos parâmetros de densidade de matéria e energia escura."""
    return 1 / E(z, Omega_M, Omega_EE)


def integracao(integral, Omega_M, Omega_EE, z):
    IntANDError = quad(integral, 0, z, args=(Omega_M, Omega_EE))
    resint = IntANDError[0]
    ERRORresint = IntANDError[1]
    return [resint, ERRORresint]


def UniType(Omega_k):
    """Determina o tipo de universo estudado baseado no valor do Parâmetro de Densidade de Curvatura(Omega_k)"""
    if Omega_k > 0:
        return "Universo Aberto"
    elif Omega_k < 0:
        return "Universo Fechado"
    else:
        return "Universo Plano"


def solution(Omega_M, Omega_EE, z, z_step):
    """Função que calcula uma matriz de resultados de distância de luminosidade (dL), módulo de distância (mu), distância de luminosidade aproximada (dLAP) e diferença entre as duas (DIF) a partir do redshift (z) e dos parâmetros de densidade de matéria e energia escura em um passo (z_step)."""
    DLvectorX = []
    DLvectorY = []
    MUvectorX = []
    MUvectorY = []
    DLAPvectorX = []
    DLAPvectorY = []
    DIFvectorX = []
    DIFvectorY = []
    for i in np.arange(float(z_step), float(z) + float(z_step), float(z_step)):
        iresint = integracao(integral, Omega_M, Omega_EE, i)
        DLvectorX.append(i)
        DLvectorY.append(dL(Omega_M, Omega_EE, iresint[0], i))
        MUvectorX.append(i)
        MUvectorY.append(mu(Omega_M, Omega_EE, iresint[0], i))
        DLAPvectorX.append(i)
        DLAPvectorY.append(approx_dL(Omega_M, Omega_EE, i))
        if i <= 1:
            DIFvectorX.append(i)
            DIFvectorY.append(DLvectorY[-1] - DLAPvectorY[-1])
    return [
        DLvectorX,
        DLvectorY,
        MUvectorX,
        MUvectorY,
        DLAPvectorX,
        DLAPvectorY,
        DIFvectorX,
        DIFvectorY,
    ]


# ? -----------------------------------------------------------------------------
# ?         FUNÇÕES SISTEMÁTICAS DE CÁLCULO NO INFERENCE
# ? -----------------------------------------------------------------------------


def chi2(mu_obs_list, ERROmu_obs_list, mu_teo_list):
    """Função responsável por calcular o qui-quadrado para uma lista de módulos de distância (mu) observados (mu_obs_list), seus erros (ERROmu_obs_list) e os módulos de distância teoricos (mu_teo_list)."""
    x = (mu_obs_list - mu_teo_list) / (ERROmu_obs_list)
    return np.sum(x**2)


def malha_mu_teo(Omega_M, Omega_EE, z_list):
    """Função responsável por calcular uma lista de módulos de distância (mu) teoricos para uma lista de redshifts (z_list)."""
    mu_teo_list = []
    for z in z_list:
        mu_teo_list.append(
            mu(
                Omega_M,
                Omega_EE,
                integracao(integral, Omega_M, Omega_EE, z)[0],
                z,
            )
        )
    return mu_teo_list


def varredura_1D(omega_list, mu_obs_list, ERROmu_obs_list, z_list):
    """Função responsável por realizar uma varredura 1D (Universo Plano) para calcular o qui-quadrado para uma lista de módulos de distância (mu) observados (mu_obs_list), seus erros (ERROmu_obs_list) e os módulos de distância teoricos (mu_teo_list)."""
    chi2_list = []
    for om in tqdm(omega_list, desc="PROGRESSO"):
        oee = 1 - om
        chi2_list.append(
            chi2(mu_obs_list, ERROmu_obs_list, malha_mu_teo(om, oee, z_list))
        )
    return [chi2_list, omega_list, 1 - np.array(omega_list)]


def varredura_2D(omegaM_list, omegaEE_list, mu_obs_list, ERROmu_obs_list, z_list):
    """Função responsável por realizar uma varredura 2D (Universo com Curvatura Livre) para calcular o qui-quadrado para uma lista de módulos de distância (mu) observados (mu_obs_list), seus erros (ERROmu_obs_list) e os módulos de distância teoricos (mu_teo_list)."""
    matriz_chi2 = np.zeros((len(omegaM_list), len(omegaEE_list)))
    for i, om in enumerate(tqdm(omegaM_list, desc="VARREDURA 2D")):
        for j, oee in enumerate(omegaEE_list):
            mu_teorico = malha_mu_teo(om, oee, z_list)
            matriz_chi2[i, j] = chi2(mu_obs_list, ERROmu_obs_list, mu_teorico)
    return matriz_chi2


def quebra_degenerecencia(
    omegaM_list, omegaEE_list, matriz_sn, omegaK_obs, ERROomegaK_obs
):
    """
    Aplica o Prior da CMB sobre a matriz de Chi2 das Supernovas.
    ok_obs e sigma_ok devem seguir o roteiro do IAG (geralmente Planck).
    """
    matriz_total = np.zeros_like(matriz_sn)
    for i, om in enumerate(omegaM_list):
        for j, oee in enumerate(omegaEE_list):
            ok_teo = 1 - (om + oee)
            chi2_cmb = ((ok_teo - omegaK_obs) ** 2) / (ERROomegaK_obs**2)
            matriz_total[i, j] = matriz_sn[i, j] + chi2_cmb
    return matriz_total


def veross(var2dPRIOR, chi2d_minPRIOR, omegaM_list, omegaEE_list):
    L_matrix = np.exp(-(var2dPRIOR - chi2d_minPRIOR) / 2)
    OM, OEE = np.meshgrid(omegaM_list, omegaEE_list, indexing='ij')
    mask_acel = OEE > (OM / 2)
    soma_total = np.sum(L_matrix)
    soma_acelerada = np.sum(L_matrix[mask_acel])
    prob_aceleracao = (soma_acelerada / soma_total)
    return prob_aceleracao