#
#! -------------------------------------------------- Bibliotecas --------------------------------------------------
from astropy import constants as const

#! -------------------------------------------------- Constantes Físicas --------------------------------------------------
H0 = 70  # Constante de Hubble [km/s/Mpc]
c = const.c.to("km/s").value  # Velocidade da luz [km/s]
#! -------------------------------------------------- Passo de Output --------------------------------------------------
z_step = 10e-4  # Distância entre um ponto e outro nos outputs gerados
