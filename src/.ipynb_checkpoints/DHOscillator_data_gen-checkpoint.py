import os
import numpy as np
from scipy.integrate import solve_ivp

def damped_spring(t, Y):
    """
    This function calculates the derivative of the state vector Y at time t
    for a spring-mass-damper system.
    t (float): time
    Y (ndarray): state vector [position, velocity]

    Returns:
    dXdt (list): derivative of state vector
    """

    # define system parameters
    m = 1.0
    k = 1.0
    c = 0.1

    return [Y[1], -k/m*Y[0] - c/m*Y[1]]

# Initial conditions
Y0 = [1.0, 0.0]

# Time span for the solution: t = [0, 30]
t_span = [0, 30]

# Time points at which the solution is to be computed.
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the system of differential equations.
sol = solve_ivp(dumped_spring, t_span, Y0, t_eval=t_eval)

# To numpy array
data = np.array([sol.t, sol.y[0], sol.y[1]]).T

# Save to file
np.save('../data/DHOscillator_data.npy', data)