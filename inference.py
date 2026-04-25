# entrada: dados_obs, mu(Omega_M, Omega_EE, resint, z),
# saida: (omega_m_bestifit,omega_ee_bestifit), matriz chiquad, deltachiquad(contorno), probabilidades integradas

from src.core import *
from src.system import *
from src.save_load import *
from main import *
from src.parameters import *

obsdatalist = load_obs_data(
    "obs_data.txt"
)
z_list = obsdatalist[0]
mu_obs_list = obsdatalist[1]
ERROmu_obs_list = obsdatalist[2]

header("Inferência de dados")
status("Iniciando a varredura 1D")

omega_list=[]
omega_var=mesh_inter_omega[0]

while omega_var<mesh_inter_omega[1]:
    omega_list.append(omega_var)
    omega_var=omega_var+meshgrid_step
varredura_1D(omega_list, mu_obs_list, ERROmu_obs_list, z_list)
status("Varredura 1D finalizada com sucesso!")
status("Iniciando exportação em dados/var1d.txt")
#todo: adicionar exportação da varredura 1D
status("Varredura 1D exportada em dados/var1d.txt com sucesso!")
status("Iniciando varredura 2D")