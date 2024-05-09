# We have to implement the bias-variance tradeoff using the polynomial regression model.
# We have to plot the graph showing the various polynomial lines with degree 1 to 10 with respect to the training data.
# We have to plot the graph showing the bias and variance tradeoff.
# We have to calculate the bias and variance for each degree of the polynomial.
# We have to print the degree, bias and variance for each degree of the polynomial.
# We have to plot the bias and variance for each degree of the polynomial.
# We have to plot the graph showing the bias and variance tradeoff.

# importing libraries
import numpy as np # for mathematical calculations
import matplotlib.pyplot as plt # for plotting the graph
from numpy.polynomial import Polynomial # for polynomial regression
import random # for generating random numbers


# dataset preparation
x = np.arange(-5, 5, 0.01) # generating x coordinates
y = 2*(x**4) - 3*(x**3) + 7*(x**2) - 23*x + 8 + np.random.normal(0, 3) # generating y coordinates
dataset = [(i, j) for i, j in zip(x, y)] # creating dataset
random.shuffle(dataset) # shuffling the dataset

# splitting the dataset into training and testing data
# 80% training data and 20% testing data
split_index = int(len(dataset) * 0.8) 
train_data = random.sample(dataset, split_index) # training data
test_data = [item for item in dataset if item not in train_data] # testing data
# separating x and y coordinates of testing data
xtest, ytest = zip(*test_data) 
# separating x and y coordinates of training data
xtrain, ytrain = zip(*train_data) 

# function to calculate polynomial coefficients
def coeff(X, Y, deg):
    # Vandermonde matrix - Adding a column of ones to the input matrix
    X_mat = np.vander(X, deg + 1, increasing=True)     
    # Transpose of the Vandermonde matrix
    XT = X_mat.T     
    # Multiplying the transpose of the Vandermonde matrix with the Vandermonde matrix
    XTX = np.matmul(XT, X_mat)    
    # Multiplying the transpose of the Vandermonde matrix with the output matrix
    XTY = np.matmul(XT, Y)     
    # Inverse of the matrix obtained by multiplying the transpose of the Vandermonde matrix with the Vandermonde matrix
    XTX_inv = np.linalg.inv(XTX)     
    # Multiplying the inverse of the matrix obtained by multiplying the transpose of the Vandermonde matrix with the Vandermonde matrix with the matrix obtained by multiplying the transpose of the Vandermonde matrix with the output matrix
    b = np.matmul(XTX_inv, XTY) 
    return b

fig = plt.figure(figsize=(20, 10)) # figure size
xplot = np.linspace(-5, 5, 10000) # generating points to plot in graph
degree = 10 # degree of the polynomial
functions = [coeff(xtrain, ytrain, i) for i in range(degree+1)] # calculating coefficients for each degree
yplot = [sum(functions[i][j] * xplot**j for j in range(len(functions[i]))) for i in range(degree+1)] # calculating y coordinates for each degree
colors = ['red', 'green', 'yellow', 'black', 'blue', 'orange', 'pink', 'purple', 'brown', 'cyan', 'magenta'] # colors for each degree
labels = ['Degree '+str(i) for i in range(degree+1)] # labels for each degree
for i in range(degree+1):
    plt.plot(xplot, yplot[i], color=colors[i], label=labels[i]) # plotting the graph
plt.scatter(xtrain, ytrain, color='blue', label='Training Data', s=10) # plotting the training data
plt.title('Graph showing the various polynomial lines with degree 1 to 10 with respect to the training data') # title of the graph
plt.xlabel('X-axis (Data Points\' x coordinates)') # x-axis label
plt.ylabel('Y-axis (Data Points\' y coordinates)') # y-axis label
plt.figtext(0.5, 0.01, 'Figure 1: We can understand that the polynomial with degree 4 almost satisfies most of the points given in the training dataset', wrap=True, horizontalalignment='center', fontsize=12) # figure text
plt.legend() # legend

fig = plt.figure(figsize=(20, 10)) # figure size
# Error calculation
def error(y, ypred):
    return sum(((y - ypred)**2))/len(y) # mean squared error
blst = [] # list to store bias
vlst = [] # list to store variance
for i in range(degree+1):
    ypredb = sum(functions[i][j] * np.array(xtrain)**j for j in range(len(functions[i]))) # predicting y values for training data
    ypredv = sum(functions[i][j] * np.array(xtest)**j for j in range(len(functions[i]))) # predicting y values for testing data
    bias = error(ytrain, ypredb) # calculating bias
    variance = error(ytest, ypredv) # calculating variance
    blst.append(bias) # appending bias to the list
    vlst.append(variance) # appending variance to the list
    print('Degree:', i+1, 'Bias:', bias, 'Variance:', variance) # printing the degree, bias and variance
plt.plot(range(0, degree+1), blst, color='red', label='Bias (Training Error)') # plotting bias
plt.plot(range(0, degree+1), vlst, color='blue', label='Variance (Testing Error)') # plotting variance
plt.legend() # legend
plt.title('Bias and Variance Tradeoff') # title of the graph
plt.xlabel('Degree of Polynomial') # x-axis label
plt.ylabel('Error (Mean Squared Error)') # y-axis label
plt.figtext(0.5, 0.01, 'Figure 2: We can understand that the bias is decreasing and variance is increasing as the degree of the polynomial increases', wrap=True, horizontalalignment='center', fontsize=12) # figure text
plt.show() # displaying the graph
# end of code