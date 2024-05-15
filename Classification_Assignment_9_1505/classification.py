# program to classify using regression
# importing the required libraries
import numpy as np
import matplotlib.pyplot as plt

# function to calcuulate the regression line
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

def indicator(lst):
    elements = list(set(lst))
    ans = []
    for i in lst:
        ans.append(elements.index(i))
    return ans

def dataset():
    # creating datasets
    x = [1, 2, 3, 4, 5, -3, -4, -5, -6] # x values
    yreal = ['B','B','B','B','B','G','G','G','G'] # y values
    y = indicator(yreal)
    return x, y

def yfun(xcoord):
    # creating datasets
    x, y = dataset()
    coeffs = coeff(x, y, 1)
    return coeffs[0] + coeffs[1]*(xcoord)

def perpendicular(xcoord):
    x, y = dataset()
    coeffs = coeff(x, y, 1)
    m = -1/coeffs[1]
    yy = sum(y)/len(y)
    xx = (yy - coeffs[0])/coeffs[1]
    d = yy - m*xx 
    return d + m*(xcoord)
    
def main():   
    # plotting the regression line
    x, y = dataset()
    xcoords = np.arange(-10, 10, 0.01)
    ycoords = np.vectorize(yfun)(xcoords)    
    avg = round(sum(y)/len(y), 2)
    fig = plt.figure(figsize=(10, 10))
    plt.plot(xcoords, ycoords, color='red', label='Regression Line')
    plt.scatter(x, y, color='blue', label='Indicator Points')   
    xd = np.arange(-10, 10, 0.01)
    ycoordsperp = np.vectorize(perpendicular)(xd)
    print('The decision boundary line is perpendicular to the regression line and passes through the threshold value at y =', avg)
    plt.plot(xd, ycoordsperp, color='green', label='Decision Boundary Line')
    plt.xlabel('X Coordinates, Scale: Linear')
    plt.ylabel('Y Coordinates, Scale: Linear')
    plt.xlim(-7, 7)
    plt.ylim(-7, 7)
    plt.legend(title = 'Legend')
    plt.title('Binary Classification')
    # Set the x and y limits to ensure the graph is not crunched
    plt.figtext(0.5, 0.01, 'Description: We found the regression line for the given points, then plotted the decision boundary line which is perpendicular to regression line and passes through the threshold value at y = '+str(avg)+'(here is it found by averaging the indication points)', wrap=True, horizontalalignment='center', fontsize=12)    
    plt.show()    

if __name__ == '__main__':
    main()