import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


x = [-3, -2, -1, 0, 1, 2, 3]
y1 = [7, 2, 0, 0, 0, 2, 7]
values = [p for p in range(-3, 4)]
b1 = list(values)
b2 = list(values)
E = []
for i in b1:
    for j in b2:
        esum = 0
        for m in range(len(x)):
            exp = (i*x[m]) + (j*((x[m])**2))
            esum += abs(y1[m] - exp)
        E.append([i, j, esum])
E.sort(key = lambda x: x[-1])
print("The Minimum E value is: ", E[0][2])
print("The corresponding beta1 value: ", E[0][0])
print("The corresponding beta2 value: ", E[0][1])

beta1, beta2, esumval = [], [], []
for row in E:
    beta1.append(row[0])
    beta2.append(row[1])
    esumval.append(row[2])

beta1 = np.array(beta1)
beta2 = np.array(beta2)
esumval = np.array(esumval)

fig = plt.figure(figsize =(5, 5))
b1 = np.array(b1)
b2 = np.array(b2)
grid_x, grid_y = np.meshgrid(b1, b2)
def fun(i, j):
    esum = 0
    for m in range(len(x)):
        exp = (i*x[m]) + (j*((x[m])**2))
        esum += abs(y1[m] - exp)
    return (esum)
grid_esumval = np.vectorize(fun)(grid_x, grid_y)
cx = plt.axes(projection='3d')
cx.plot_surface(grid_x, grid_y, grid_esumval)
cx.set_xlabel('Beta1')
cx.set_ylabel('Beta2')
cx.set_zlabel('E values')
cx.set_title('Surface Plot of E Values for Beta1 and Beta2')
plt.show()