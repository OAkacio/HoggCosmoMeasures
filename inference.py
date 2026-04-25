# entrada: dados_obs, mu(Omega_M, Omega_EE, resint, z),
# saida: (omega_m_bestifit,omega_ee_bestifit), matriz chiquad, deltachiquad(contorno), probabilidades integradas

from src.core import *
from src.system import *
from src.save_load import *
from main import *
from src.parameters import *
from src.plot import *

obsdatalist = load_obs_data("obs_data.txt")
z_list = obsdatalist[0]
mu_obs_list = obsdatalist[1]
ERROmu_obs_list = obsdatalist[2]
header("Inferência de dados")
status("Iniciando a varredura 1D")
omega_list = []
omega_var = mesh_inter_omega[0]
while omega_var < mesh_inter_omega[1]:
    omega_list.append(omega_var)
    omega_var = omega_var + meshgrid_step
var1d = varredura_1D(omega_list, mu_obs_list, ERROmu_obs_list, z_list)
status("Varredura 1D finalizada com sucesso!")
chi_min = np.min(var1d[0])
INDchi_min = np.argmin(var1d[0])
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
param(
    "Densidade de materia 1_sigma_esquerda (L_1_sigma_Omega_M)",
    var1d[1][L_INDchi_sigma1],
)
param(
    "Densidade de energia 1_sigma_esquerda (L_1_sigma_Omega_EE)",
    var1d[2][L_INDchi_sigma1],
)
param(
    "Densidade de materia 1_sigma_direita (R_1_sigma_Omega_M)",
    var1d[1][R_INDchi_sigma1],
)
param(
    "Densidade de energia 1_sigma_direita (R_1_sigma_Omega_EE)",
    var1d[2][R_INDchi_sigma1],
)
param("Qui-quadrado 2_sigma (chi2_2_sigma)", chi_sigma2)
param(
    "Densidade de materia 2_sigma_esquerda (L_2_sigma_Omega_M)",
    var1d[1][L_INDchi_sigma2],
)
param(
    "Densidade de energia 2_sigma_esquerda (L_2_sigma_Omega_EE)",
    var1d[2][L_INDchi_sigma2],
)
param(
    "Densidade de materia 2_sigma_direita (R_2_sigma_Omega_M)",
    var1d[1][R_INDchi_sigma2],
)
param(
    "Densidade de energia 2_sigma_direita (R_2_sigma_Omega_EE)",
    var1d[2][R_INDchi_sigma2],
)
param("Qui-quadrado 3_sigma (chi2_3_sigma)", chi_sigma3)
param(
    "Densidade de materia 3_sigma_esquerda (L_3_sigma_Omega_M)",
    var1d[1][L_INDchi_sigma3],
)
param(
    "Densidade de energia 3_sigma_esquerda (L_3_sigma_Omega_EE)",
    var1d[2][L_INDchi_sigma3],
)
param(
    "Densidade de materia 3_sigma_direita (R_3_sigma_Omega_M)",
    var1d[1][R_INDchi_sigma3],
)
param(
    "Densidade de energia 3_sigma_direita (R_3_sigma_Omega_EE)",
    var1d[2][R_INDchi_sigma3],
)
status("Cálculo de incertezas finalizado!")
status("Iniciando criação de gráfico de distribuição qui-quadrado")
plot(True, var1d[1], var1d[0], "distQuiQuad", r"$\Omega_M$", r"$\chi^2$")
status("Criação de gráficos finalizada!")
status("Iniciando a varredura 2D")
omegaM_list = []
omegaM_var = mesh_inter_omega[0]
while omegaM_var < mesh_inter_omega[1]:
    omegaM_list.append(omegaM_var)
    omegaM_var = omegaM_var + meshgrid_step
omegaEE_list = omegaM_list
var2d = varredura_2D(omegaM_list, omegaEE_list, mu_obs_list, ERROmu_obs_list, z_list)
status("Varredura 2D finalizada com sucesso!")
chi2d_min = np.min(var2d)
MINDchi2d_min, EEINDchi2d_min = np.unravel_index(np.argmin(var2d), var2d.shape)
param("Qui-quadrado mínimo (2dchi2_min)", chi2d_min)
param("Densidade de materia Bestfit (2dBF_Omega_M)", omegaM_list[MINDchi2d_min])
param("Densidade de energia Bestfit (2dBF_Omega_EE)", omegaEE_list[EEINDchi2d_min])
status("Iniciando cálculo de incertezas")
chi2d_sigma1 = chi2d_min + 2.30
chi2d_sigma2 = chi2d_min + 6.18
chi2d_sigma3 = chi2d_min + 11.83
niveis = [chi2d_sigma1, chi2d_sigma2, chi2d_sigma3]
elipse_plot(True, omegaM_list, omegaEE_list, var2d, niveis, "elipse_var")
status("Iniciando quebra de degenerescência: Aplicando Prior da CMB na malha 2D")
var2dPRIOR = quebra_degenerecencia(
    omegaM_list, omegaEE_list, var2d, Omega_K_obs, ERROOmega_K_obs
)
status("Quebra de degenerecência finalizada com sucesso!")
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
niveisPRIOR = [chi2d_sigma1PRIOR, chi2d_sigma2PRIOR, chi2d_sigma3PRIOR]
elipse_plot(True, omegaM_list, omegaEE_list, var2dPRIOR, niveisPRIOR, "elipsePRIOR_var")
status("Iniciando cálculo da probabilidade de aceleração")
prob_aceleracao = veross(var2dPRIOR, chi2d_minPRIOR, omegaM_list, omegaEE_list)
if prob_aceleracao > 0.997:
    acel = "confirmada!"
else:
    acel = "não confirmada!"
param("Probabilidade de Aceleração (P_acel)", prob_aceleracao)
param("Aceleração do universo superior a 3-sigma", acel)
