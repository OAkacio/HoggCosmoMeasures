# entrada: dados_obs, mu(Omega_M, Omega_EE, resint, z),
# saida: (omega_m_bestifit,omega_ee_bestifit), matriz chiquad, deltachiquad(contorno), probabilidades integradas

from src.core import *
from src.system import *
from src.save_load import *
from main import *
from src.parameters import *

obsdatalist = load_obs_data(
    "obs_data.txt"
)  # carrega uma matriz com os vetores [z], [mu], [ERROmu]
z_list = obsdatalist[0]
mu_obs_list = obsdatalist[1]
ERROmu_obs_list = obsdatalist[2]