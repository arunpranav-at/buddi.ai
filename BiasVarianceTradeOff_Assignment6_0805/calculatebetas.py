import numpy as np
import matplotlib.pyplot as plt
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
    yplot = np.sum(coeffs[i] * xplot**i for i in range(len(coeffs)))
    plt.plot(xplot, yplot, color=color, label=label)

# Plotting different degree polynomials
plot_polynomial(1, 'red', 'Degree 1')
plot_polynomial(2, 'green', 'Degree 2')
plot_polynomial(3, 'yellow', 'Degree 3')
plot_polynomial(4, 'black', 'Degree 4')

plt.legend()

# Plotting Bias Variance Trade Off
fig = plt.figure(figsize=(20, 10))

xtest, ytest = zip(*list_20_percent)
def bias_variance_tradeoff(deg):
    coeffs = calculate_coefficients(xtrain, ytrain, deg)
    ypred_train = np.sum([coeffs[i] * xtrain**i for i in range(len(coeffs))], axis=0)

    bias = np.mean(np.abs(ytrain - ypred_train))
    
    ypred_test = np.sum(coeffs[i] * xtest**i for i in range(len(coeffs)))
    variance = np.mean(np.abs(ytest - ypred_test))
    
    return bias, variance

deg_range = np.arange(1, 10, 1)
bias_values = []
variance_values = []

for deg in deg_range:
    bias, variance = bias_variance_tradeoff(deg)
    bias_values.append(bias)
    variance_values.append(variance)

plt.plot(deg_range, bias_values, color='blue', label='Training Error (Bias)')
plt.plot(deg_range, variance_values, color='red', label='Test Error (Variance)')
plt.legend()
plt.show()
