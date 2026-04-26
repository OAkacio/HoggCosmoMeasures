#
# * =============================================================================
# * DEPENDÊNCIAS
# * =============================================================================

# ? -----------------------------------------------------------------------------
# ?         MÓDULOS LOCAIS
# ? -----------------------------------------------------------------------------

from src.core import *
from src.system import *
from src.save_load import *
from main import *
from src.parameters import *
from src.plot import *

# * =============================================================================
# * ROTINA PRINCIPAL
# * =============================================================================

obsdatalist = load_obs_data("obs_data.txt")
z_list = obsdatalist[0]
mu_obs_list = obsdatalist[1]
ERROmu_obs_list = obsdatalist[2]
header("Inferência de dados", Dados="obs_data.txt")

# ? -----------------------------------------------------------------------------
# ?         VARREDURA UNIDIMENSIONAL
# ? -----------------------------------------------------------------------------

status("Iniciando a varredura 1D")
omega_list = []
omega_var = mesh_inter_omega[0]
while omega_var < mesh_inter_omega[1]:
    omega_list.append(omega_var)
    omega_var = omega_var + meshgrid_step
var1d = varredura_1D(omega_list, mu_obs_list, ERROmu_obs_list, z_list, w)
chi_min = np.min(var1d[0])
INDchi_min = np.argmin(var1d[0])
status("Iniciando cálculo de parâmetros da varredura 1D")
param("Qui-quadrado mínimo (chi2_min)", chi_min)
param("Densidade de materia Bestfit (BF_Omega_M)", var1d[1][INDchi_min])
param("Densidade de energia Bestfit (BF_Omega_EE)", var1d[2][INDchi_min])
status("Iniciando cálculo de incertezas")
chi_sigma1 = chi_min + 1
chi_sigma2 = chi_min + 4
chi_sigma3 = chi_min + 9
R_INDchi_sigma1 = np.abs(var1d[0][INDchi_min:] - chi_sigma1).argmin() + INDchi_min
L_INDchi_sigma1 = np.abs(var1d[0][:INDchi_min] - chi_sigma1).argmin()
R_INDchi_sigma2 = np.abs(var1d[0][INDchi_min:] - chi_sigma2).argmin() + INDchi_min
L_INDchi_sigma2 = np.abs(var1d[0][:INDchi_min] - chi_sigma2).argmin()
R_INDchi_sigma3 = np.abs(var1d[0][INDchi_min:] - chi_sigma3).argmin() + INDchi_min
L_INDchi_sigma3 = np.abs(var1d[0][:INDchi_min] - chi_sigma3).argmin()
param("Qui-quadrado 1_sigma (chi2_1_sigma)", chi_sigma1)
param("Qui-quadrado 2_sigma (chi2_2_sigma)", chi_sigma2)
param("Qui-quadrado 3_sigma (chi2_3_sigma)", chi_sigma3)
status("Iniciando criação de gráfico de distribuição qui-quadrado")
plot(True, var1d[1], var1d[0], "distQuiQuad", r"$\Omega_M$", r"$\chi^2$")

# ? -----------------------------------------------------------------------------
# ?         PROBABILIDADE DE ENERGIA ESCURA
# ? -----------------------------------------------------------------------------

status("Iniciando cálculo da probabilidade de (Omega_EE > 0.5)")
prob_ee = veross1d(var1d[0], chi_min, var1d[2])
if prob_ee > 0.5:
    ee1d = "confirmada!"
else:
    ee1d = "não confirmada!"
param("Probabilidade de Energia Escura (P_ee)", prob_ee)
param("Energia Escura do universo superior a 50%", ee1d)
space()

# ? -----------------------------------------------------------------------------
# ?         VARREDURA BIDIMENSIONAL
# ? -----------------------------------------------------------------------------

status("Iniciando a varredura 2D")
omegaM_list = []
omegaM_var = mesh_inter_omega[0]
while omegaM_var < mesh_inter_omega[1]:
    omegaM_list.append(omegaM_var)
    omegaM_var = omegaM_var + meshgrid_step
omegaEE_list = omegaM_list
var2d = varredura_2D(omegaM_list, omegaEE_list, mu_obs_list, ERROmu_obs_list, z_list, w)
chi2d_min = np.min(var2d)
MINDchi2d_min, EEINDchi2d_min = np.unravel_index(np.argmin(var2d), var2d.shape)
status("Iniciando cálculo de parâmetros da varredura 2D")
param("Qui-quadrado mínimo (2dchi2_min)", chi2d_min)
param("Densidade de materia Bestfit (2dBF_Omega_M)", omegaM_list[MINDchi2d_min])
param("Densidade de energia Bestfit (2dBF_Omega_EE)", omegaEE_list[EEINDchi2d_min])
status("Iniciando cálculo de incertezas")
chi2d_sigma1 = chi2d_min + 2.30
chi2d_sigma2 = chi2d_min + 6.18
chi2d_sigma3 = chi2d_min + 11.83
param("Qui-quadrado 1_sigma (chi2_1_sigma)", chi2d_sigma1)
param("Qui-quadrado 2_sigma (chi2_2_sigma)", chi2d_sigma2)
param("Qui-quadrado 3_sigma (chi2_3_sigma)", chi2d_sigma3)
niveis = [chi2d_sigma1, chi2d_sigma2, chi2d_sigma3]
status("Iniciando criação de gráfico de distribuição qui-quadrado")
elipse_plot(True, omegaM_list, omegaEE_list, var2d, niveis, "elipse_var")

# ? -----------------------------------------------------------------------------
# ?         QUEBRA DE DEGENERECÊNCIA (PRIOR DA CMB)
# ? -----------------------------------------------------------------------------

status("Iniciando quebra de degenerescência: Aplicando Prior da CMB na malha 2D")
var2dPRIOR = quebra_degenerecencia(
    omegaM_list, omegaEE_list, var2d, Omega_K_obs, ERROOmega_K_obs
)
chi2d_minPRIOR = np.min(var2dPRIOR)
MINDchi2d_minPRIOR, EEINDchi2d_minPRIOR = np.unravel_index(
    np.argmin(var2dPRIOR), var2dPRIOR.shape
)
param(
    "Qui-quadrado mínimo com quebra de degenerecência (2dchi2_minPRIOR)", chi2d_minPRIOR
)
param(
    "Densidade de materia Bestfit com quebra de degenerecência (2dBF_Omega_MPRIOR)",
    omegaM_list[MINDchi2d_minPRIOR],
)
param(
    "Densidade de energia Bestfit com quebra de degenerecência (2dBF_Omega_EEPRIOR)",
    omegaEE_list[EEINDchi2d_minPRIOR],
)
status("Iniciando cálculo de incertezas")
chi2d_sigma1PRIOR = chi2d_minPRIOR + 2.30
chi2d_sigma2PRIOR = chi2d_minPRIOR + 6.18
chi2d_sigma3PRIOR = chi2d_minPRIOR + 11.83
param("Qui-quadrado 1_sigma (chi2_1_sigma)", chi2d_sigma1PRIOR)
param("Qui-quadrado 2_sigma (chi2_2_sigma)", chi2d_sigma2PRIOR)
param("Qui-quadrado 3_sigma (chi2_3_sigma)", chi2d_sigma3PRIOR)
niveisPRIOR = [chi2d_sigma1PRIOR, chi2d_sigma2PRIOR, chi2d_sigma3PRIOR]
status("Iniciando criação de gráfico de distribuição qui-quadrado")
elipse_plot(True, omegaM_list, omegaEE_list, var2dPRIOR, niveisPRIOR, "elipsePRIOR_var")

# ? -----------------------------------------------------------------------------
# ?         PROBABILIDADE DE ACELERAÇÃO 2D
# ? -----------------------------------------------------------------------------

status("Iniciando cálculo da probabilidade de aceleração")
prob_aceleracao = veross2d(var2dPRIOR, chi2d_minPRIOR, omegaM_list, omegaEE_list, w)
if prob_aceleracao > 0.997:
    acel = "confirmada!"
else:
    acel = "não confirmada!"
param("Probabilidade de Aceleração (P_acel)", prob_aceleracao)
param("Aceleração do universo superior a 3-sigma", acel)
space()

# ? -----------------------------------------------------------------------------
# ?         VARREDURA BIDIMENSIONAL - OMEGA_M VS W
# ? -----------------------------------------------------------------------------

status("Iniciando varredura bidimensional (OMEGA_M vs W)")
w_list = []
w_var = mesh_inter_w[0]
while w_var < mesh_inter_w[1]:
    w_list.append(w_var)
    w_var = w_var + meshgrid_step
var2dOW = varreduraOW(w_list, omegaM_list, mu_obs_list, ERROmu_obs_list, z_list)
chi2dOW_min = np.min(var2dOW)
WINDchi2dOW_min, MINDchi2dOW_min = np.unravel_index(np.argmin(var2dOW), var2dOW.shape)
status("Iniciando cálculo de parâmetros da varredura 2D (w vs Omega_M)")
param("Qui-quadrado mínimo (2dchi2_min)", chi2dOW_min)
param("Parâmetro da equação de estado Bestfit (2dBF_w)", w_list[WINDchi2dOW_min])
param("Densidade de matéria Bestfit (2dBF_Omega_M)", omegaM_list[MINDchi2dOW_min])
status("Iniciando cálculo de incertezas")
chi2dOW_sigma1 = chi2dOW_min + 2.30
chi2dOW_sigma2 = chi2dOW_min + 6.18
chi2dOW_sigma3 = chi2dOW_min + 11.83
param("Qui-quadrado 1_sigma (chi2_1_sigma)", chi2dOW_sigma1)
param("Qui-quadrado 2_sigma (chi2_2_sigma)", chi2dOW_sigma2)
param("Qui-quadrado 3_sigma (chi2_3_sigma)", chi2dOW_sigma3)
niveis = [chi2dOW_sigma1, chi2dOW_sigma2, chi2dOW_sigma3]
status("Iniciando criação de gráfico de distribuição qui-quadrado")
elipse_plot(
    True, w_list, omegaM_list, var2dOW, niveis, "elipse_varOW", r"$w$", r"$\Omega_M$"
)

status("EXECUÇÃO FINALIZADA!")
