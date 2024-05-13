# Gradient Descent - Assignment 7 - 09/05/2024
Problem statement: Calculate the b0 and b1 values for a set of points where b0 and b1 represents the coefficients of the linear equation from which the points are taken. After calculating, compare with the b0 and b1 value obtained from Closed Form.<br>

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

Code: Refer gradientdescent.py in GradientDescent_Assignment7_0905 folder <br>
To install required libraries:
```
pip install matplotlib, random, numpy
```
Move into the GradientDescent_Assignment7_0905 and then run the python program gradientdescent.py
```
cd GradientDescent_Assignment7_0905
python3 gradientdescent.py
python3 gradientdescentb0b1epoch.py
```
Run the python file directly without entering into the directory using the below code
```
python3 GradientDescent_Assignment7_0905/gradientdescent.py
python3 GradientDescent_Assignment7_0905/gradientdescentb0b1epoch.py
```
Note: The folder path conventions and other details followed are respect to Linux OS, users using Windows OS are required to change file paths and other requirements as needed for Windows OS. <br>

Output: Error vs Epoch Graph. We can understand that the error decreases with increase in number of epochs. <br>
![gradientdescent](<../Pictures/outputgradientdescent.png>) <br>
![gradientdescent](<../Pictures/gradientdescent_epochvserror.png>) <br>
![gradientdescent](<../Pictures/betavaluesvsepoch.png>) <br>