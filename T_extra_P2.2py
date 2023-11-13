# Uma torre de congelamento de ervilhas pode ser modelada aproximadamente como um duto vertical (g=9,81 [m/s2]) na qual a temperatura é mantida em toda a sua seção a T_infinity=-30 [C]. Existe uma corrente ascendente de ar com velocidade de 10 m/s na qual a Força de Arrasto, F_d, sobre uma ervilha pode ser modelada pela equação: "

# F_d=C_d*((rho_f*V_rel^2*A)/2)

# g=9,81 [m/s^2]
# T_infinity = -30 [C]
# V_ar= 10 [m/s]
# rho_f = 1,23 [kg/m^3]
# mu = 1,5E-5 [kg/(ms)] 
# T_0=0 [C]
# Vo= 0 [m/s]
# T_1= -20 [C]
# D = 5E-3 [m]
 # rho_gelo= 920 [kg/ m^3]
# k= 2,2 [W/(mK)]
# c= 2040 [J/(kgK)]
# h = 40 [W/(m^2*K)]

# Onde C_D é o coeficiente de arrasto, rho_f é a massa específica do ar escoando ( rho_f = 1,23 kg/m^33), V_rel é a velocidade do ar relativo a ervilha, A [m^2] é a área da seção transversal do corpo esférico (ervilha). O coeficiente de arrasto é expresso como: "

# C_D=24/R_e
# R_e=(rho_f*V_rel*D)/mu

# sendo Re o número de Reynolds e D o diâmetro da esfera e  mu = 1,5 .10^-5 [kg/(sm)] é a viscosidade dinâmica. Considere, nesta primeira análise, que a ervilha entra nesta seção do túnel de resfriamento, já congelada a temperatura de 0ºC, partindo do repouso (Vo= 0 m/s). Opondo-se a este deslocamento existe uma Força de Arraste. Determine (assumindo a hipótese de capacitância global válida): 

# a)	Utilizando a 2ª Lei de Newton: sumF = m(dV/dt),calcule o comprimento do túnel, L, a fim de que as ervilhas saiam a uma temperatura de -20ºC. Assuma que o diâmetro da ervilha é 5 [mm] e suas propriedades são próximas ao do gelo [rho_gelo= 920 [kg/ m3], k= 2,2 [W/(mK)] e c= 2040 [J/(kgK)]]. O coeficiente de convecção médio neste problema é h = 40 [W/(m^2*K)]
# b)	Para as mesmas condições, calcule a energia de resfriamento necessária para uma vazão de 5 [kg/s] de ervilha. 
# c)	A hipótese de capacitância global é válida nesta condição? 


import math
import scipy.integrate as spi

# Constants
g = 9.81  # m/s^2
T_infinity = -30  # C
V_ar = 10  # m/s
rho_f = 1.23  # kg/m^3
mu = 1.5E-5  # kg/(ms)
T_0 = 0  # C
Vo = 0  # m/s
T_1 = -20  # C
D = 5E-3  # m
rho_gelo = 920  # kg/m^3
k = 2.2  # W/(mK)
c = 2040  # J/(kgK)
h = 40  # W/(m^2*K)
A = math.pi * D**2  # m^2

# Calculate Reynolds number
Re = (rho_f * V_ar * D) / mu

# Calculate drag coefficient
Cd = 24 / Re

# Calculate drag force
Fd = Cd * ((rho_f * V_ar**2 * A) / 2)

# Calculate the mass of the pea
m = rho_gelo * (4/3) * math.pi * (D/2)**3

# Calculate the acceleration of the pea
a = Fd / m

# Calculate the time it takes for the pea to reach the desired temperature
t = (T_1 - T_0) / (h * A / (rho_gelo * c))

# Calculate the length of the tunnel
L = a * t**2 / 2

print(f"A) The length of the tunnel is {L} m.")

# Given
m_dot = 5  # kg/s

# Calculate the energy required for cooling
Q = m_dot * c * (T_0 - T_1)

print(f"B) The energy required for cooling is {Q} J/s or Watts.")


# Given
d = D  # diameter of the pea, m

# Calculate the characteristic length (volume/surface area for a sphere)
L_c = (3/4) * d

# Calculate the Biot number
Bi = h * L_c / k

print(f"The Biot number is {Bi}.")

if Bi < 0.1:
    print("C) The lumped capacitance model is valid.")
else:
    print("The lumped capacitance model is not valid.")
