import os
import numpy as np
from scipy.integrate import solve_ivp

def lorenz(t, Y):
    # documentation
    """
    This function returns the right-hand side of the Lorenz system of ordinary differential equations.
    Parameters:
    t (float): time
    Y (array): state vector [x, y, z]

    Returns:
    array: [dxdt, dydt, dzdt]
    """

    x, y, z = Y
    dxdt = 10 * (y - x)
    dydt = x * (28 - z) - y
    dzdt = x * y - 8/3 * z

    return [dxdt, dydt, dzdt]

# initial conditions
Y0 = [-11.78361808,   3.52735854,  12.35618245]

# time span
t_span = [0, 8]

# Time points where the solution is to be computed.
t_eval = np.linspace(0, 8, 1000)

# solve the ODE
sol = solve_ivp(lorenz, t_span, Y0, t_eval=t_eval, atol=1e-16, rtol=3e-14)

# To numpy array
data = np.array([sol.t, sol.y[0], sol.y[1], sol.y[2]]).T

# Save to file
np.save("../data/Lorenz_data.npy", data)