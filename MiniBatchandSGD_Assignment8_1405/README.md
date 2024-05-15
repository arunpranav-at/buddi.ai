# Gradient Descent - Assignment 8 - 14/05/2024
Problem statement: Calculate the b0 and b1 values for a set of points where b0 and b1 represents the coefficients of the linear equation from which the points are taken Using Mini Batch Gradient Descent and Stochastic Gradient Descent. After calculating, compare with the b0 and b1 value obtained from Closed Form.<br>

Solution: We generate x coordinates using 
```
x = np.arange(-10, 10, 0.01) 
```
and corresponding y coordinates using 
```
y = 2*x - 3 + np.random.normal(0, 5). 
```
We then initialize b0 and b1 values randomly using 
```
np.random.normal(0, 1)
```

Code: Refer sgd.py, minibatch.py in MiniBatchSGD_Assignment8_1405 folder <br>
To install required libraries:
```
pip install matplotlib, random, numpy
```
Move into the MiniBatchSGD_Assignment8_1405 and then run the python program sgd.py, minibatch.py
```
cd MiniBatchSGD_Assignment8_1405
python3 sgd.py
python3 minibatch.py
```
Run the python file directly without entering into the directory using the below code
```
python3 MiniBatchSGD_Assignment8_1405/sgd.py
python3 MiniBatchSGD_Assignment8_1405/minibatch.py
```
Note: The folder path conventions and other details followed are respect to Linux OS, users using Windows OS are required to change file paths and other requirements as needed for Windows OS. <br>

Output: Error vs Epoch Graph. We can understand that the error decreases with increase in number of epochs both in Mini Batch Gradient Descent and Stochastic Gradient Descent. <br><br>

Mini Batch Gradient Descent <br>
![minibatchgradientdescent](<../Pictures/minibatchoutput.png>) <br>
![minibatchgradientdescent](<../Pictures/minibatch.png>) <br><br>
Stochastic Gradient Descent <br>
![minibatchgradientdescent](<../Pictures/sgdoutput.png>) <br>
![stochasticgradientdescent](<../Pictures/sgd.png>) <br>