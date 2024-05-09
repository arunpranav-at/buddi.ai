import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random
import math

#creating 100 data points
x = np.arange(-10, 10, 0.1)
def pointfun(x):
    return 2*(x**4) - 3*(x**3) + 7*(x**2) - 23*x + 8 + np.random.normal(0, 3)
y = np.vectorize(pointfun)(x)

my_list = [(i,j) for i,j in zip(x,y)]

# Shuffle the list
random.shuffle(my_list)

# Calculate the split index based on the desired percentages
split_index = int(len(my_list) * 0.8)

# Split the list into 80% and 20% parts
list_80_percent = random.sample(my_list, split_index)
list_20_percent = [item for item in my_list if item not in list_80_percent]

fig = plt.figure(figsize =(20, 10))
xtrain, ytrain = zip(*list_80_percent)
plt.scatter(xtrain, ytrain, color='blue', label='Training Data', s = 10)

xplot = np.linspace(-10, 10, 10000)

# Fit the data with a polynomial of degree 1
f1 = Polynomial.fit(xtrain, ytrain, 1)
plt.plot(xplot, f1(xplot), color='red', label='Degree 1')

# Fit the data with a polynomial of degree 2
f2 = Polynomial.fit(xtrain, ytrain, 2)
plt.plot(xplot, f2(xplot), color='green', label='Degree 2')

# Fit the data with a polynomial of degree 3
f3 = Polynomial.fit(xtrain, ytrain, 3)
plt.plot(xplot, f3(xplot), color='yellow', label='Degree 3')

# Fit the data with a polynomial of degree 4
f4 = Polynomial.fit(xtrain, ytrain, 4)
plt.plot(xplot, f4(xplot), color='black', label='Degree 4')

# Lagrange Polynomial Line
# X = np.array(xtrain)
# Y = np.array(ytrain)

# n = len(X)
# poly = Polynomial(np.zeros(n))

# for j in range(n):
#     k = [k for k in range(n) if k != j]
#     roots = -1 * X[k]

#     sub_poly = Polynomial.fromroots(X[k])
#     scale = Y[j] / np.prod(X[j] - X[k])
#     sub_poly.coef *= scale

#     poly.coef += sub_poly.coef
# yplot = []
# xnew = []
# for i in xplot:
#     if -200<=poly(i)<=2500:
#         yplot.append(poly(i))
#         xnew.append(i)
# yplot = np.array(yplot)
# xnew = np.array(xnew)
# plt.plot(xnew, yplot, color='purple', label='Lagrange Polynomial Line')

plt.legend()

fig = plt.figure(figsize =(20, 10))
xtrain = np.array(xtrain)
ytrain = np.array(ytrain)

# Plotting Bias Variance Trade Off
def biasCalculation(deg):
    pdeg = Polynomial.fit(xtrain, ytrain, deg)
    ypred = np.vectorize(pdeg)(xtrain)
    return sum(abs(ytrain - ypred))/len(ytrain)

deg = np.arange(1, 20, 1) 
error = np.vectorize(biasCalculation)(deg)
plt.plot(deg, error, color='blue', label='Training Error (Bias)')

xtest, ytest = zip(*list_20_percent)
xtest = np.array(xtest)
ytest = np.array(ytest)

def varianceCalculation(deg):
    pdeg = Polynomial.fit(xtrain, ytrain, deg)
    ypred = np.vectorize(pdeg)(xtest)
    return sum(abs(ytest - ypred))/len(ytest)

error = np.vectorize(varianceCalculation)(deg)
plt.plot(deg, error, color='red', label='Test Error (Variance)')    
plt.legend()
plt.show()

