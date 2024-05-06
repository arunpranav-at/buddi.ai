import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import random
import math

total = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
pivalues = [0, 0, 0, 0, 0, 0, 0]
inside = 0
for i in range(total[-1]+1):
    x = random.uniform(-0.5, 0.5)
    y = random.uniform(-0.5, 0.5)
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
plt.ylabel('Estimated PI Values')
plt.xlabel('Number of Darts')
plt.title('Estimated PI Values vs Number of Darts using Uniform Random Samples')
plt.legend(title='Legend\nX Axis: Logarithmic Scale\nY Axis: Linear Scale\nPI Value: 3.14159265358979323846...')

description = "This graph shows the estimated values of PI using a Monte Carlo simulation based on the number of random points (darts thrown) generated.\nWe can understand that more the number of darts thrown, the estimated value of PI gets closer to the actual value of PI."
plt.figtext(0.5, 0.001, description, ha='center', fontsize=10, bbox=dict(facecolor='lightgray', alpha=0.5))

plt.show()