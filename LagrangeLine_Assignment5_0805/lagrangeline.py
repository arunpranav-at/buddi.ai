import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt

X = np.array([-3, -2, -1, 0, 1, 2, 3])
Y = np.array([7, 2, 0, 0, 0, 2, 7])

n = len(X)
poly = Polynomial(np.zeros(n))

for j in range(n):
    k = [k for k in range(n) if k != j]
    roots = -1 * X[k]

    sub_poly = Polynomial.fromroots(X[k])
    scale = Y[j] / np.prod(X[j] - X[k])
    sub_poly.coef *= scale

    poly.coef += sub_poly.coef

fig = plt.figure(figsize =(20, 10))
plt.scatter(X, Y)
Xinterp = np.linspace(min(X), max(X), 100)
plt.plot(Xinterp, poly(Xinterp), label='Lagrange Polynomial Line')
plt.title('Plotting Lagrange Polynomial Line for the given data points')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend(title='Legend')
plt.figtext(0.5, 0.01, 'We are plotting the Lagrange Polynomial Line for the given seven data points. Lagrange Polynomial Line passes through all the given data points hence the E (epsilon) value would be zero. But if unseen data points are given, Lagrange Polynomial Line need to be changed. It would be performing poorly for new data points.', wrap=True, horizontalalignment='center', fontsize=12)
plt.show()