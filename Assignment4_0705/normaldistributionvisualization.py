import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import random
import math

def fun(x, u, s):
    return (math.exp(-0.5 * (((x - u) / s)**2))) / (s * math.sqrt(2 * math.pi)) #normal distribution function

ulst = [-4, -3, -2, -1, 0, 1, 2, 3, 4] #mean values
slst = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5] #standard deviation values
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'pink', 'orange']
u = 0
fig = plt.figure(figsize =(8, 8))
for s in slst:
    x = np.arange(-10, 10, 0.001)
    y = np.vectorize(fun)(x, u, s)
    plt.plot(x, y, label = f'Normal Distribution with \u03c3 value {s}', color = colors[slst.index(s)])
plt.title('Normal Distribution with same Mean \u03bc = 0 and different Standard Deviation values')
plt.xlabel('\u03bc values (Mean)')
plt.ylabel('Y values (Probability Density Function)')
plt.legend(title='Legend')
plt.figtext(0.5, 0.01, 'We are plotting normal distribution curve for same mean and different standard deviation values. We observe that the position of peak doesnot change as it is dependent on Mean and height and width of peak changes as it is dependent on Standard Deviation', wrap=True, horizontalalignment='center', fontsize=12)

s = 1
fig = plt.figure(figsize =(8, 8))
for u in ulst:
    x = np.arange(-10, 10, 0.001)
    y = np.vectorize(fun)(x, u, s)
    plt.plot(x, y, label = f'Normal Distribution with \u03bc value {u}', color = colors[ulst.index(u)])
plt.title('Normal Distribution with same Standard Deviation \u03c3 = 1 and different Mean values')
plt.xlabel('\u03bc values (Mean)')
plt.ylabel('Y values (Probability Density Function)')
plt.xticks(np.arange(-10, 10, 1))
plt.legend(title='Legend')
plt.figtext(0.5, 0.01, 'We are plotting normal distribution curve for same standard deviation and different mean values. We observe that the height and width of peak doesnot change as it is dependent on Standard Deviation and position of peak changes as it is dependent on Mean', wrap=True, horizontalalignment='center', fontsize=12)
plt.show()
    
            
        
        
        
