import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def lorenz(t, x):
    X, Y, Z = x
    dX = s * (Y - X)
    dY = X * (r - Z) - Y
    dZ = X * Y - b * Z
    return dX, dY, dZ


s = 10
b = 8 / 3
r = 28

t_span = 0, 40
t_eval = np.linspace(t_span[0], t_span[1], 20000)
x0 = [1.0, 1.0, 1.0]
sol = solve_ivp(lorenz, t_span, x0, t_eval=t_eval)

ax = plt.gcf().add_subplot(111, projection='3d')
plt.plot(sol.y[0], sol.y[1], sol.y[2])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("l63.png")
