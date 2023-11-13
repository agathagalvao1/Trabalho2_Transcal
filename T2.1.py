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
h = 30  # Convection coefficient in W/(m^2-K)

# Time intervals
dt_values = [0.1, 1, 10]  # Time step sizes in seconds
t_max = 1000  # Maximum time for simulation in seconds

# Function to calculate temperature at each time step
def calculate_temperature(dt):
    n_steps = int(t_max / dt)
    T = np.zeros(n_steps)
    T[0] = T0
    for n in range(1, n_steps):
        T[n] = T[n-1] + (4 * dt / (rho * np.pi * D**2 * cp)) * (-h * np.pi * D * (T[n-1] - T_infinity) - epsilon * sigma * np.pi * D * (T[n-1]**4 - T_viz**4) + R * i**2)
    return T

# Calculate steady-state temperature
def steady_state(T_RP):
    return 4 / (rho * np.pi * D**2 * cp) * (-h * np.pi * D * (T_RP - T_infinity) - epsilon * sigma * np.pi * D * (T_RP**4 - T_viz**4) + R * i**2)
T_RP = fsolve(steady_state, T0)

# Calculate and plot temperature for each time step size
plt.figure()
for dt in dt_values:
    T = calculate_temperature(dt)
    plt.plot(np.arange(0, t_max, dt), T, label=f'dt={dt}s')

plt.plot([0, t_max], [T_RP, T_RP], 'k--', label='Steady state')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.legend()
plt.show()
