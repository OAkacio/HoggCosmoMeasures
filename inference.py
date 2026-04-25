# entrada: dados_obs, mu(Omega_M, Omega_EE, resint, z),
# saida: (omega_m_bestifit,omega_ee_bestifit), matriz chiquad, deltachiquad(contorno), probabilidades integradas

from src.core import *
from src.system import *
from src.save_load import *
from main import *

obsdatalist = load_obs_data("obs_data.txt")
meshgrid_i = [0, 0]  # omega_m,omega_ee
meshgrid_f = [1, 1]  # omega_m,omega_ee
meshgrid_step = 10e-3  # omega_m,omega_ee

...