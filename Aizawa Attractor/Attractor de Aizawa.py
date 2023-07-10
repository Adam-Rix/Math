import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
num_steps = 20000

a = 0.95
b = 0.7
c = 0.6
d = 3.5
e = 0.25
f = 0.1

def aizawa_transform(val):
    x = val[0]
    y = val[1]
    z = val[2]

    x1 = (z - b) * x - d * y
    y1 = d * x + (z - b) * y
    z1 = c + a * z - (z ** 3)/3 - (x**2 + y**2) * (1 + e * z) + f * z * (x ** 3)

    t = [x + dt * x1, y + dt * y1, z + dt * z1]

    return t

# Initialization of the initial point
x0, y0, z0 = 0.1, 0.1, 0.1
points = [[x0, y0, z0]]

# Computing a sequence of points using the Aizawa transformation
for _ in range(num_steps):
    point = aizawa_transform(points[-1])
    points.append(point)

# Separation of point coordinates
x = [point[0] for point in points]
y = [point[1] for point in points]
z = [point[2] for point in points]

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
