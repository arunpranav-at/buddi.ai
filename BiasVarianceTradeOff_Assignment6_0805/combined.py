import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
import random

# dataset preparation
x = np.arange(-5, 5, 0.01)
y = 2*(x**4) - 3*(x**3) + 7*(x**2) - 23*x + 8 + np.random.normal(0, 3)
dataset = [(i, j) for i, j in zip(x, y)]
random.shuffle(dataset)
split_index = int(len(dataset) * 0.8)
train_data = random.sample(dataset, split_index)
test_data = [item for item in dataset if item not in train_data]
xtest, ytest = zip(*test_data)
xtrain, ytrain = zip(*train_data)

# function to calculate polynomial coefficients
def calculate_coefficients(X, Y, deg):
    X_mat = np.vander(X, deg + 1, increasing=True)
    XT = X_mat.T
    XTX = XT.dot(X_mat)
    XTY = XT.dot(Y)
    XTX_inv = np.linalg.inv(XTX)
    b = XTX_inv.dot(XTY)
    return b

# function to calculate coefficients
def coeff(deg):
    coeffs = calculate_coefficients(xtrain, ytrain, deg)
    return coeffs

# plotting the polynomial lines
fig = plt.figure(figsize=(20, 10))
xplot = np.linspace(-5, 5, 10000)    
degree = 10
functions = [coeff(i) for i in range(degree+1)]
yplot = [sum(functions[i][j] * xplot**j for j in range(len(functions[i]))) for i in range(degree+1)]
colors = ['red', 'green', 'yellow', 'black', 'blue', 'orange', 'pink', 'purple', 'brown', 'cyan', 'magenta']
labels = ['Degree '+str(i) for i in range(degree+1)]
for i in range(degree+1):
    plt.plot(xplot, yplot[i], color=colors[i], label=labels[i])
plt.scatter(xtrain, ytrain, color='blue', label='Training Data', s=10)
plt.title('Graph showing the various polynomial lines with degree 1 to 10 with respect to the training data')
plt.xlabel('X-axis (Data Points\' x coordinates)')
plt.ylabel('Y-axis (Data Points\' y coordinates)')
plt.figtext(0.5, 0.01, 'Figure 1: We can understand that the polynomial with degree 4 almost satisfies most of the points given in the training dataset', wrap=True, horizontalalignment='center', fontsize=12)
plt.legend()

fig = plt.figure(figsize=(20, 10))
# Error calculation
def error(y, ypred):
    return sum(((y - ypred)**2))/len(y)
blst = []
vlst = []
for i in range(degree+1):
    ypredb = sum(functions[i][j] * np.array(xtrain)**j for j in range(len(functions[i])))
    ypredv = sum(functions[i][j] * np.array(xtest)**j for j in range(len(functions[i])))    
    bias = error(ytrain, ypredb)
    variance = error(ytest, ypredv)
    blst.append(bias)
    vlst.append(variance)
    print('Degree:', i+1, 'Bias:', bias, 'Variance:', variance)
plt.plot(range(0, degree+1), blst, color='red', label='Bias (Training Error)')
plt.plot(range(0, degree+1), vlst, color='blue', label='Variance (Testing Error)') 
plt.legend()
plt.title('Bias and Variance Tradeoff')
plt.xlabel('Degree of Polynomial')
plt.ylabel('Error (Mean Squared Error)')
plt.figtext(0.5, 0.01, 'Figure 2: We can understand that the bias is decreasing and variance is increasing as the degree of the polynomial increases', wrap=True, horizontalalignment='center', fontsize=12)
plt.show()
    
