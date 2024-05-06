import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import random
import math
from scipy.interpolate import make_interp_spline, BSpline

total = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
pivalues = [0, 0, 0, 0, 0, 0, 0]
inside = 0
for i in range(total[-1]+1):
    x = np.random.normal(0, 3)
    while -0.5 > x or x > 0.5:
        x = np.random.normal(0, 3)
    y = np.random.normal(0, 3)
    while -0.5 > y or y > 0.5:
        y = np.random.normal(0, 3)
    dis = math.sqrt(x**2 + y**2)
    if dis <= 0.5:
        inside += 1
    if i in total:
        pi = 4 * (inside/i)
        print("Estimated value of pi when number of darts are ", i, "is :", pi)
        pivalues[total.index(i)] = pi

fig = plt.figure(figsize =(8, 8))
plt.axhline(y=math.pi, color = 'black', linestyle='--', label='PI Value with Highest Precision')
plt.plot(total, pivalues, marker='o', label='Estimated PI Values')
plt.xscale('log')
plt.yscale('linear')
plt.ylabel('Estimated PI Values (Linear Scale)')
plt.xlabel('Number of Darts (Logarithmic Scale)')
plt.title('Estimated PI Values vs Number of Darts using Normal Samples')
plt.legend(title='Legend\nPI Value: 3.14159265358979323846...')

description = "This graph shows the estimated values of PI using a Monte Carlo simulation based on the number of random points (darts thrown) generated.\nWe can understand that more the number of darts, the estimated value of PI gets closer to the actual value of PI."
plt.figtext(0.5, 0.001, description, ha='center', fontsize=10, bbox=dict(facecolor='lightgray', alpha=0.5))

plt.show()

