import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
num_points = 80000

a = 0.208186
b = 0.083
c = 0.308186
d = 0.32
e = 0.1
f = 0.8

# Initialization of the starting point
x = np.zeros(num_points)
y = np.zeros(num_points)
z = np.zeros(num_points)

# Initial coordinate values
x[0] = 0.1
y[0] = 0.1
z[0] = 0.1

# Calculation of the sequence of points
for i in range(1, num_points):
    x1 = (z[i-1] - b) * x[i-1] - d * y[i-1]
    y1 = d * x[i-1] + (z[i-1] - b) * y[i-1]
    z1 = c + a * z[i-1] - (z[i-1] ** 3) / 3 - (x[i-1] ** 2 + y[i-1] ** 2) * (1 + e * z[i-1]) + f * z[i-1] * (x[i-1] ** 3)
    x[i] = x[i-1] + dt * x1
    y[i] = y[i-1] + dt * y1
    z[i] = z[i-1] + dt * z1

# Visualization of the attractor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, '.', markersize=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Thomas Attractor')
plt.show()
