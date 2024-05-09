import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
import random

# Creating 100 data points
x = np.arange(-5, 5, 0.1)
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

fig = plt.figure(figsize=(20, 10))
xtrain, ytrain = zip(*list_80_percent)
xtest, ytest = zip(*list_20_percent)
plt.scatter(xtrain, ytrain, color='blue', label='Training Data', s=10)

xplot = np.linspace(-5, 5, 10000)

# Function to calculate polynomial coefficients using the formula
def calculate_coefficients(X, Y, deg):
    # Create the Vandermonde matrix X
    X_mat = np.vander(X, deg + 1, increasing=True)
    XT = X_mat.T
    XTX = XT.dot(X_mat)
    XTY = XT.dot(Y)
    XTX_inv = np.linalg.inv(XTX)
    b = XTX_inv.dot(XTY)
    return b

# Plotting the polynomial lines without using the Polynomial function
def plot_polynomial(deg, color, label):
    coeffs = calculate_coefficients(xtrain, ytrain, deg)
    yplot = sum(coeffs[i] * xplot**i for i in range(len(coeffs)))
    plt.plot(xplot, yplot, color=color, label=label)

# Plotting different degree polynomials
colors = ['red', 'green', 'yellow', 'black']
labels = ['Degree 1', 'Degree 2', 'Degree 3', 'Degree 4']

for i in range(4):
    plot_polynomial(i+1, colors[i], labels[i])

plt.title('Graph showing the various polynomial lines with degree 1, 2, 3 and 4 with respect to the training data')
plt.figtext(0.5, 0.01, 'Figure 1: We can understand that the polynomial with degree 4 almost satisfies most of the points given in the training dataset', wrap=True, horizontalalignment='center', fontsize=12)
plt.xlabel('X-axis (Data Points\' x coordinates)')
plt.ylabel('Y-axis (Data Points\' y coordinates)')
plt.legend()

fig = plt.figure(figsize =(20, 10))
xtrain = np.array(xtrain)
ytrain = np.array(ytrain)

# Plotting Bias Variance Trade Off
def biasCalculation(deg):
    pdeg = Polynomial.fit(xtrain, ytrain, deg)
    ypred = np.vectorize(pdeg)(xtrain)
    return sum(abs(ytrain - ypred))/len(ytrain)

deg = np.arange(1, 10, 1) 
berror = np.vectorize(biasCalculation)(deg)

xtest, ytest = zip(*list_20_percent)
xtest = np.array(xtest)
ytest = np.array(ytest)

# Extract X and Y from the split lists
X, Y = xtrain, ytrain
X = np.array(X)
Y = np.array(Y)
n = len(X)

# Compute Lagrange coefficients
def lagrange_coefficients(x, X, i):
    n = len(X)
    p = 1
    for j in range(n):
        if j != i:
            p *= (x - X[j]) / (X[i] - X[j])
    return p

# Compute Lagrange polynomial
def lagrange_poly(x, X, Y):
    n = len(X)
    poly = 0
    for i in range(n):
        poly += Y[i] * lagrange_coefficients(x, X, i)
    return poly
Xinterp = np.linspace(min(X), max(X), 100)
Eb = np.mean((Y - lagrange_poly(X, X, Y))**2)
ypred = lagrange_poly(np.array(xtest), X, Y)
E = np.mean((ypred - ytest)**2)

def varianceCalculation(deg):
    pdeg = Polynomial.fit(xtrain, ytrain, deg)
    ypred = np.vectorize(pdeg)(xtest)
    return sum(abs(ytest - ypred))/len(ytest)

verror = np.vectorize(varianceCalculation)(deg)
deg = np.append(deg, 101)
verror = np.append(verror, E)
berror = np.append(berror, Eb)
plt.plot(deg, berror, color='blue', label='Training Error (Bias)')
plt.plot(deg, verror, color='red', label='Test Error (Variance)')    
plt.legend()
plt.title('Graph showing the Bias and Variance trade off with respect to the training and test data')
plt.figtext(0.5, 0.01, 'Figure 2: We can understand that the training error decreases as the degree of the polynomial increases and the test error also decreases as the degree of the polynomial increases', wrap=True, horizontalalignment='center', fontsize=12)
plt.xlabel('Degree of the Polynomial')
plt.xticks(np.arange(1, 10, 1))
plt.ylabel('Error (Bias and Variance)')
plt.show()