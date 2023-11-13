import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Given data
i = 1  # Current in Amps
R = 100  # Resistance in Ohms/m
D = 0.005  # Diameter in m
T0 = 20 + 273.15  # Initial temperature in K
T_infinity = T0  # Ambient temperature in K
T_viz = T0  # Surrounding temperature in K
epsilon = 0.7  # Emissivity
rho = 8933  # Density in kg/m^3
cp = 385  # Specific heat in J/kg-K
sigma = 5.670374419E-8  # Stefan-Boltzmann constant in W/(m^2-K^4)
h_values = [1, 10, 100]  # Convection coefficients in W/(m^2-K)

# Time interval
dt = 0.1  # Time step size in seconds
t_max = 1000  # Maximum time for simulation in seconds

# Function to calculate temperature at each time step
def calculate_temperature(h, dt):
    n_steps = int(t_max / dt)
    T = np.zeros(n_steps)
    T[0] = T0
    for n in range(1, n_steps):
        T[n] = T[n-1] + (4 * dt / (rho * np.pi * D**2 * cp)) * (-h * np.pi * D * (T[n-1] - T_infinity) - epsilon * sigma * np.pi * D * (T[n-1]**4 - T_viz**4) + R * i**2)
    return T

# Calculate steady-state temperature
def steady_state(T_RP, h):
    return 4 / (rho * np.pi * D**2 * cp) * (-h * np.pi * D * (T_RP - T_infinity) - epsilon * sigma * np.pi * D * (T_RP**4 - T_viz**4) + R * i**2)

# Calculate and plot temperature for each convection coefficient
plt.figure()
for h in h_values:
    T_RP = fsolve(steady_state, T0, args=(h))
    T = calculate_temperature(h, dt)
    plt.plot(np.arange(0, t_max, dt), T, label=f'h={h} W/(m^2-K)')

plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.legend()
plt.show()
