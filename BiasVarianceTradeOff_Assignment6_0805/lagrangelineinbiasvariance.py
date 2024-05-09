import numpy as np
import matplotlib.pyplot as plt
import random

# Generate synthetic data
xdata = np.arange(-10, 10, 0.1)
def pointfun(x):
    return 2*(x**4) - 3*(x**3) + 7*(x**2) - 23*x + 8 + np.random.normal(0, 3)
ydata = np.vectorize(pointfun)(xdata)

my_list = [(i, j) for i, j in zip(xdata, ydata)]
# Shuffle the list
random.shuffle(my_list)
# Calculate the split index based on the desired percentages
split_index = int(len(my_list) * 0.8)
# Split the list into 80% and 20% parts
list_80_percent = random.sample(my_list, split_index)
list_20_percent = [item for item in my_list if item not in list_80_percent]

# Extract X and Y from the split lists
X, Y = zip(*list_80_percent)
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

# Plotting
fig = plt.figure(figsize=(20, 8))
plt.scatter(X, Y, color='blue', label='Data Points', s=10)
Xinterp = np.linspace(min(X), max(X), 100)
plt.plot(Xinterp, lagrange_poly(Xinterp, X, Y), label='Lagrange Polynomial Line', color='red')
plt.title('Plotting Lagrange Polynomial Line for the given data points')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend(title='Legend')

Eb = np.mean((Y - lagrange_poly(X, X, Y))**2)
print('Training Error for the Lagrange Polynomial Line (Bias):', Eb)
# Error calculation
xtest, ytest = zip(*list_20_percent)
ypred = lagrange_poly(np.array(xtest), X, Y)
E = np.mean((ypred - ytest)**2)
print('Testing Error for the Lagrange Polynomial Line (Variance):', E)

# Annotate the plot with error information
des = '. We are plotting the Lagrange Polynomial Line for the given data points using the Lagrange interpolation formula.'
plt.figtext(0.5, 0.01,"Bias = "+str(Eb) +" Variance = " + str(E) + des, wrap=True, horizontalalignment='center', fontsize=12)
plt.show()