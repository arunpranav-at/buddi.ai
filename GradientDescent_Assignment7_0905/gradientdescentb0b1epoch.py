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
    yclosed = eb0 + eb1*x # predicted values using closed form
    errorclosed = mse(y, yclosed) # error using closed form
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
    b0lst = [b0] # list to store b0 values
    b1lst = [b1] # list to store b1 values
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
        # appending the b0 value to the list
        b0lst.append(b0)
        # appending the b1 value to the list
        b1lst.append(b1)
        
        # checking the convergence
        if abs(error - nerror) < 10e-6:
            flag = False
        else:
            error = nerror
            
    # printing the values of b0, b1, error and epoch
    print("Using The Closed Form :", "b0:", eb0, "b1:", eb1, "error:", errorclosed)
    print("Using GradientDescent :", "b0:", b0, "b1:", b1, "error:", error, "epoch:", epoch)
    
    # plotting the error vs epoch graph
    fig = plt.figure(figsize=(20,8)) # creating a figure size of 20x8
    plt.plot(epochlst, b0lst, label = "b0 values", color = 'r') # plotting the graph for b0 values
    plt.plot(epochlst, b1lst, label = "b1 values", color = 'b') # plotting the graph for b1 values
    plt.xlabel('Epoch (Number of times the Gradient Descent is carried out) Scale: Linear Scale') # x-axis label
    plt.ylabel('Beta Values (Coefficients) Scale: Linear Scale') # y-axis label
    plt.axhline(y=eb0, color='r', linestyle='--', label = "b0 value by Closed Form") # horizontal line for b0 value by closed form
    plt.axhline(y=eb1, color='b', linestyle='--', label = "b1 value by Closed Form") # horizontal line for b1 value by closed form
    plt.legend(title = "Legend" ) # legend
    plt.title('Beta Values vs Epoch Graph for Gradient Descent') # title
    plt.figtext(0.5, 0.01, 'Figure 1: Beta Values vs Epoch Graph. We can understand that the beta values become accurate with increase in number of epochs.', ha='center') # description
    
    b0lst = np.array(b0lst) # converting the list to numpy array
    b1lst = np.array(b1lst) # converting the list to numpy array
    epochlst = np.array(epochlst) # converting the list to numpy array
    errorlst = np.array(errorlst) # converting the list to numpy array
    fig = plt.figure(figsize=(20,8)) # creating a figure size of 20x8
    cx = plt.axes(projection='3d')
    cx.plot_trisurf(b0lst, b1lst, epochlst, cmap='viridis') # plotting the surface plot
    cx.set_xlabel('Beta0')
    cx.set_ylabel('Beta1')
    cx.set_zlabel('Epochs')
    cx.set_title('Surface Plot of Beta0 and Beta1 for each Epochs')
    cx.legend(['b0 and b1 values'], title='Legend')
    description = "This surface plot shows the different Beta0(b0) and Beta1(b1) values at different Epochs.\nThe increase in Epochs result in accurate Beta0 and Beta1 values."
    fig.text(0.5, 0.05, description, ha='center', fontsize=12)
    
    fig = plt.figure(figsize=(20,8)) # creating a figure size of 20x8
    cx = plt.axes(projection='3d')
    cx.plot_trisurf(b0lst, b1lst, errorlst, cmap='viridis') # plotting the surface plot
    cx.set_xlabel('Beta0')
    cx.set_ylabel('Beta1')
    cx.set_zlabel('Error (MSE)')
    cx.set_title('Surface Plot of Beta0 and Beta1 and MSE')
    cx.legend(['b0 and b1 values'], title='Legend')
    description = "This surface plot shows the different Beta0(b0) and Beta1(b1) values with different Errors.\nThe increase in ppochs result in accurate Beta0 and Beta1 values and decrease in error."
    fig.text(0.5, 0.05, description, ha='center', fontsize=12)
    plt.show() # displaying the plot
    

if __name__ == "__main__":
    main() # calling the main function