# Program to visualize the working of gradient descent algorithm

# importing libraries
import numpy as np # for mathematical calculations
import matplotlib.pyplot as plt # for plotting the graphs
import random # for generating random numbers

# function to generate y values with respect to x values
def yfunction(x): 
    return 2*x - 3 + np.random.normal(0, 5) # y values function

# function to calculate polynomial coefficients for closed form
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

# function for calculating the mean square error
def mse(y, ycap):
    # squared difference between actual and predicted values and taking the mean
    return np.mean((y - ycap)**2)

def main():
    # creating datasets
    x = np.arange(-10, 10, 0.01) # x values
    y = np.vectorize(yfunction)(x) # y values
  
    # define degree of the polynomial
    degree = 1
    # obtaining beta values using closed form to compare
    eb0, eb1 = coeff(x, y, 1) # b0 and b1 values by closed form

    # gradient descent processing
    ib0 = np.random.normal(0, 1) #initial selecting b0 value randomly
    ib1 = np.random.normal(0, 1) #initial selecting b1 value randomly

    ierror = mse(y, ib0 + ib1*x) # initial error
    lr = 0.01 # learning rate - also called by the name eta

    error = ierror # initialising error
    b0 = ib0 # initialising b0
    b1 = ib1 # initialising b1
    epoch = 0 # initialising epoch
    epochlst = [0] # list to store epoch values
    errorlst = [ierror] # list to store error values
    
    flag = True # flag to check the convergence
    while flag: # loop until convergence
        # calculating the predicted values using the initial values of b0 and b1
        ycap = b0 + b1*x
        
        # calculating the gradient of the error with respect to b0 and b1
        grad0 = -2*np.mean((y - ycap)) #differentiating the error with respect to b0
        grad1 = -2*np.mean((y - ycap)*x) #differentiating the error with respect to b1
        
        # updating the values of b0 and b1
        b0 = b0 - lr*grad0
        b1 = b1 - lr*grad1
        
        # calculating the new error using the updated values of b0 and b1
        nerror = mse(y, b0 + b1*x)
        
        # incrementing the epoch
        epoch += 1 
        
        # appending the epoch value to the list
        epochlst.append(epoch) 
        # appending the error value to the list
        errorlst.append(error)    
        
        # checking the convergence
        if abs(error - nerror) < 10e-6:
            flag = False
        else:
            error = nerror
            
    # printing the values of b0, b1, error and epoch
    print("Using The Closed Form :", "b0:", eb0, "b1:", eb1, "error:", ierror)
    print("Using GradientDescent :", "b0:", b0, "b1:", b1, "error:", error, "epoch:", epoch)
    
    # plotting the error vs epoch graph
    fig = plt.figure(figsize=(20,8)) # creating a figure size of 20x8
    plt.plot(epochlst, errorlst, label = "Mean Square Error") # plotting the graph
    plt.xlabel('Epoch (Number of times the Gradient Descent is carried out) Scale: Linear Scale') # x-axis label
    plt.ylabel('Error (Mean Square Error) Scale: Linear Scale') # y-axis label
    plt.legend(title = "Legend" ) # legend
    plt.title('Error vs Epoch Graph for Gradient Descent') # title
    plt.figtext(0.5, 0.01, 'Figure 1: Error vs Epoch Graph. We can understand that the error decreases with increase in number of epochs.', ha='center') # description
    plt.show() # displaying the plot
    

if __name__ == "__main__":
    main() # calling the main function