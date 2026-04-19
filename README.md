# FLRW Luminosity Distance Integrator

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Este repositório contém um integrador numérico desenvolvido em Python para o cálculo da Distância de Luminosidade ($d_L$) em modelos cosmológicos de Friedmann-Lemaître-Robertson-Walker (FLRW). O código permite a superposição e comparação de diferentes modelos de universo (Matéria, Energia Escura e Benchmark).

## Autoria

Victor Moreira Acacio

Institute of Astronomy, Geophysics and Atmospheric Sciences of the University of São Paulo

GitHub: @OAkacio

ORCID: 0009-0007-4484-2129

## Instalação

Clone este repositório e instale as dependências executando os seguintes códigos no terminal:

git clone https://github.com/OAkacio/flrw-luminosity-distance-integrator.git

cd flrw-luminosity-distance-integrator

pip install -r requirements.txt

## Uso

Para rodar a rotina de integração completa, gerar os arquivos de dados .txt para os três modelos base e plotar os gráficos de superposição, execute:

python main.py

## Base Teórica

A fundamentação teórica deste integrador baseia-se nas definições clássicas de distâncias cosmológicas para um modelo de Friedmann-Lemaître-Robertson-Walker (FLRW), conforme sumarizado na literatura padrão de cosmografia. O código calcula as grandezas em cascata:

**1. Função de Expansão de Hubble ($E(z)$)**
A evolução da taxa de expansão do universo em função do redshift $z$ é descrita por $E(z)$, que depende dos parâmetros de densidade de matéria ($\Omega_m$), curvatura ($\Omega_k$) e energia escura ($\Omega_{EE}$), considerando a sua equação de estado $w$:

$$E(z) = \sqrt{\Omega_m(1+z)^3 + \Omega_k(1+z)^2 + \Omega_{EE}(1+z)^{3(1+w)}}$$

**2. Distância Comóvel Radial ($D_C$)**
Representa a distância percorrida pela luz ao longo da linha de visada, sendo o alvo da integração numérica principal:

$$D_C = \frac{c}{H_0} \int_0^z \frac{dz'}{E(z')}$$

**3. Distância Comóvel Transversal ($D_M$)**
Leva em conta a geometria do universo. Sendo a distância de Hubble $D_H = c/H_0$, a distância transversal é determinada pelo parâmetro de curvatura espacial ($\Omega_k = 1 - \Omega_m - \Omega_{EE}$):

$$D_M = \begin{cases} \frac{D_H}{\sqrt{\Omega_k}} \sinh\left(\sqrt{\Omega_k} \frac{D_C}{D_H}\right) & \text{se } \Omega_k > 0 \text{ (Universo Aberto)} \\ D_C & \text{se } \Omega_k = 0 \text{ (Universo Plano)} \\ \frac{D_H}{\sqrt{|\Omega_k|}} \sin\left(\sqrt{|\Omega_k|} \frac{D_C}{D_H}\right) & \text{se } \Omega_k < 0 \text{ (Universo Fechado)} \end{cases}$$

**4. Distância de Luminosidade ($D_L$)**
Relaciona a luminosidade absoluta de um objeto com o fluxo observado na Terra, sendo o parâmetro-chave para o estudo de "velas padrão" (como as supernovas):

$$D_L = (1+z) D_M$$

**5. Módulo de Distância ($\mu$)**
A relação logarítmica entre a magnitude aparente e absoluta, representando o observável astronômico direto da simulação:

$$\mu = 5 \log_{10}\left(D_L\right) + 25$$
*(Onde $D_L$ é expressa em Megaparsecs - Mpc).*


## Estrutura do Projeto

```text
├── data/           # Dados gerados (.txt)
├── figures/        # Gráficos de superposição (.png)
├── src/            # Módulos principais (core.py, parameters.py, plot.py, save_load.py)
├── main.py         # Motor de integração e gerador de dados
└── requirements.txt
```

## Motivação

Este repositório foi desenvolvido como parte de um projeto de cosmologia focado no estudo de supernovas. O objetivo central para esse código é fornecer uma rotina open-source e reprodutível para a integração numérica da distância de luminosidade, permitindo a comparação direta do comportamento da expansão do universo sob diferentes parâmetros de densidade de matéria e energia escura.

## Referências

O desenvolvimento da fundamentação matemática deste integrador, bem como as equações de cascatas para distâncias cosmológicas, foram fortemente baseados em:

* HOGG, David W. **Distance measures in cosmology**. 1999. Disponível em: [https://arxiv.org/abs/astro-ph/9905116](https://arxiv.org/abs/astro-ph/9905116).