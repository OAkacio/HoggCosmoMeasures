#-------------------------------------------------- Bibliotecas --------------------------------------------------

from astropy import constants as const

# -------------------------------------------------- Parâmetros de Entrada --------------------------------------------------

H0 = 68  # Constante de Hubble [km/s/Mpc]
Omega_M = 0.3  # Densidade de matéria [adm.]
Omega_EE = 0.7  # Densidade de energia escura [adm.]
c=const.c.to('km/s').value  # Velocidade da luz [km/s]
w=-1 # Parâmetro de equação de estado da energia escura [adm.]
z=10 # Redshift máximo [adm.]