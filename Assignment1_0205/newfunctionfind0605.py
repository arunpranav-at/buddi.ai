import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

x = [-3, -2, -1, 0, 1, 2, 3]
y1 = [7, 2, 0, 0, 0, 2, 7]

b1 = np.arange(-1, 1, 0.001)
b2 = np.arange(-1, 1, 0.001)
fig = plt.figure(figsize =(10, 10))
grid_x, grid_y = np.meshgrid(b1, b2)
minib1, minib2, miniesum = 0, 0, 100000

def fun(i, j):
    global miniesum
    global minib1
    global minib2
    esum = 0
    for m in range(len(x)):
        exp = (i*x[m]) + (j*((x[m])**2))
        esum += abs(y1[m] - exp)
    if esum < miniesum:
        miniesum = esum
        minib1 = i
        minib2 = j
    return (esum)

grid_esumval = np.vectorize(fun)(grid_x, grid_y)
cx = plt.axes(projection='3d')
cx.plot_surface(grid_x, grid_y, grid_esumval)
cx.set_xlabel('Beta1')
cx.set_ylabel('Beta2')
cx.set_zlabel('E values')
cx.set_title('Surface Plot of E Values for Beta1 and Beta2')

print("The Minimum E value is: ", round(miniesum, 3))
print("The corresponding beta1 value: ", round(minib1, 3))
print("The corresponding beta2 value: ", round(minib2, 3))

plt.show()