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
    xset = np.arange(-5, 5, 0.01) # x values
    yset = np.vectorize(yfunction)(xset) # y values
    dataset = list(zip(xset, yset)) # zipping the x and y values
    #suffling the dataset
    random.shuffle(dataset)
    #training and testing data
    datatrain = dataset[:int(0.8*len(dataset))] # 80% of the dataset is training data
    datatest = dataset[int(0.8*len(dataset)):] # 20% of the dataset is testing data
    
    x = np.array([i[0] for i in datatrain]) # x values of the training data
    y = np.array([i[1] for i in datatrain]) # y values of the training data
    xt = np.array([i[0] for i in datatest]) # x values of the testing data
    yt = np.array([i[1] for i in datatest]) # y values of the testing data
    fig = plt.figure(figsize=(20,8)) # creating a figure size of 20x8
    # define degree of the polynomial
    degree = 1
    # obtaining beta values using closed form to compare
    eb0, eb1 = coeff(x, y, 1) # b0 and b1 values by closed form
    yclosed = eb0 + eb1*x # predicted values using closed form
    errorclosed = mse(y, yclosed) # error using closed form
    # gradient descent processing
    ib0 = np.random.normal(0, 1) #initial selecting b0 value randomly
    ib1 = np.random.normal(0, 1) #initial selecting b1 value randomly
    ierrort = mse(yt[0], ib0 + ib1*xt[0]) # initial error for testing data
    ierror = mse(y[0], ib0 + ib1*x[0]) # initial error
    lrlst = [0.001] # learning rate - also called by the name eta
    colorslst = ['r', 'b', 'g', 'black'] # colors for plotting the graphs
    for i in range(len(lrlst)): # loop for different learning rates
        # initialising the values
        lr = lrlst[i] # learning rate
        error = ierror # initialising error
        b0 = ib0 # initialising b0
        b1 = ib1 # initialising b1
        epoch = 0 # initialising epoch
        epochlst = [0] # list to store epoch values
        errorlst = [ierror] # list to store error values
        errortlst = [ierrort]
        flag = True # flag to check the convergence
        while flag: # loop until convergence
            for j in range(1, len(x)): # loop for each data point
                # calculating the predicted values using the initial values of b0 and b1
                ycap = b0 + b1*x[j]
                
                # calculating the gradient of the error with respect to b0 and b1
                grad0 = -2*(y[j] - ycap) #differentiating the error with respect to b0
                grad1 = -2*(y[j] - ycap)*x[j] #differentiating the error with respect to b1
                
                # updating the values of b0 and b1
                b0 = b0 - lr*grad0
                b1 = b1 - lr*grad1
                                
                # calculating the new error using the updated values of b0 and b1
                nerror = mse(y, b0 + b1*x)
                errort = mse(yt, b0 + b1*xt)   
                    
                # appending the error value to the list
                errorlst.append(nerror)  
                                
                # appending the error value calculated using the testing data
                errortlst.append(errort)  
                
                # incrementing the epoch   
                epoch += 1
                # appending the epoch value to the list
                epochlst.append(epoch)
                
            # checking the convergence
            if abs(error - nerror) < 10e-6:
                flag = False
            else:
                error = nerror            
        epochlst = [i/len(x) for i in epochlst]     
        # printing the values of b0, b1, error and epoch
        print("Using The Closed Form :", "b0:", eb0, "b1:", eb1, "error:", errorclosed)
        print("Using Stochastic Gradient Descent :", "b0:", b0, "b1:", b1, "error:", error, "epoch:", epoch//len(x), "learning rate:", lr)
        
        # plotting the error vs epoch graph
        plt.plot(epochlst[20:], errorlst[20:], label = "MSE for Training Dataset, Learning Rate: "+str(lr), color = colorslst[i]) # plotting the graph
        plt.plot(epochlst[20:], errortlst[20:], label = "MSE for Testing Dataset, Learning Rate: "+str(lr), color = colorslst[len(colorslst) - i - 1]) # plotting the graph
    plt.xlabel('Epoch (Number of times the Gradient Descent is carried out) Scale: Linear Scale') # x-axis label
    plt.ylabel('Error (Mean Square Error) Scale: Linear Scale') # y-axis label
    plt.xlim(0, 2) # setting the limits for x-axis
    plt.legend(title = "Legend") # legend
    plt.title('Error vs Epoch Graph for Stochastic Gradient Descent') # title
    plt.figtext(0.5, 0.01, 'Figure 1: Error vs Epoch Graph. We can understand that the error decreases with increase in number of epochs.', ha='center') # description
    plt.show() # displaying the plot
    

if __name__ == "__main__":
    main() # calling the main function