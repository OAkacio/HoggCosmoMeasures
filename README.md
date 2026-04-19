# FLRW Luminosity Distance Integrator

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Este repositório contém um integrador numérico desenvolvido em Python para o cálculo da Distância de Luminosidade ($d_L$) em modelos cosmológicos de Friedmann-Lemaître-Robertson-Walker (FLRW). O código permite a superposição e comparação de diferentes modelos de universo (Matéria, Energia Escura e Benchmark).

## Base Teórica

A distância de luminosidade é calculada integrando a função de expansão de Hubble $E(z)$:

$$E(z) = \sqrt{\Omega_m(1+z)^3 + \Omega_k(1+z)^2 + \Omega_\Lambda}$$

A distância comóvel radial é dada por:

$$d_C = \frac{c}{H_0} \int_0^z \frac{dz'}{E(z')}$$

## Estrutura do Projeto

├── data/           # Dados gerados (.txt)
├── figures/        # Gráficos de superposição (.png)
├── src/            # Módulos principais (core.py, parameters.py, etc.)
├── main.py         # Motor de integração CLI
├── analysis.py     # Script para superposição de gráficos
└── requirements.txt

## Instalação

Clone este repositório e instale as dependências:
git clone https://github.com/SeuUsuario/flrw-luminosity-distance-integrator.git
cd flrw-luminosity-distance-integrator
pip install -r requirements.txt

## Autoria

## Motivação

##