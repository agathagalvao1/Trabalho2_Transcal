# Definindo as variáveis
t_ar = 10  # Temperatura do ar em graus Celsius
L = 7.00  # Comprimento do reservatório em metros
W = 3.90  # Largura do reservatório em metros
h = 1.50  # Profundidade média do reservatório em metros
k = 0.0263  # Condutividade térmica em W/(mK)
alpha = 22.5e-6  # Coeficiente de expansão térmica em m^2/s
upsilon = 15.89e-6  # Viscosidade cinemática em m^2/s
P_r = 0.707  # Número de Prandtl

# Para a água a 35°C
v_l = 0.001007  # Volume específico do líquido em m^3/kg
v_v = 22.93  # Volume específico do vapor em m^3/kg
h_l = 2414  # Entalpia do líquido em kJ/kg

# Para a difusão Ar-Água
D_AB = 0.26e-4  # Coeficiente de difusão em m^2/s

# Calculando o número de Reynolds
R_e = (alpha * L) / upsilon

# Usando a correlação para calcular Nmu_bar_L
Nmu_bar_L = 0.037 * R_e ** (4/5) * P_r ** (1/3)

# Calculando a perda de calor por convecção livre
q_conv = Nmu_bar_L * k * (35 - t_ar) / L

print(f"A) A perda térmica por convecção livre é {Nmu_bar_L:.2f} W/m²K.")


for UR in [0, 50, 100]:
    # A razão de umidade do ar varia com a umidade relativa
    x = (UR / 100) * v_v / (1 + v_v)

    # A quantidade de água evaporada por segundo
    g_s = alpha * L * W * (v_v - x) / 3600

    # O calor fornecido
    q = h_l * g_s

    # O calor fornecido pela evaporação
    q_evap = h_l * g_s

    # A capacidade do aquecedor é a soma das perdas de calor por convecção e evaporação
    q_heater = q_conv + q_evap

     
    print(f"B) A perda térmica por evaporação para UR={UR}% é {q} kW.")
    print(f"C) A taxa de evaporação para UR={UR}% é {g_s} kg/s.")
    print(f"D) Capacidade do aquecedor UR={UR}% é {q_heater} kW.")
