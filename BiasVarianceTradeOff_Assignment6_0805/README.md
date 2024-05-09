# Bias Variance Trade Off - Assignment 6 - 08/05/2024
Problem statement: Generate (x,y) coordinates using the function 2(x^4) - 3(x^3) + 7(x^2) - 23x + 8 + N(0, 3). Suffle the data, take 80% points as training dataset and 20% points as testing dataset. Plot different polynomial functions with degrees 1, 2, 3, 4 .... and compare Bias(Training Error) Variance(Testing Error) Trade Off<br>

Solution: We are supposed to plot bias and variance for different models which are nothing but the polynomial functions of degrees 1, 2, 3, 4 .... Then compare Bias and Variance<br>

Code: Refer calculatebetas.py and numpybiasvariancetradeoff.py in BiasVarianceTradeOff_Assignment6_0805 folder <br>
To install required libraries:
```
pip install matplotlib, numpy, math, random
```
Move into the BiasVarianceTradeOff_Assignment6_0805
```
cd BiasVarianceTradeOff_Assignment6_0805/
```
Run the python file
```
python3 BiasVarianceTradeOff_Assignment6_0805/numpybiasvariancetradeoff.py
python3 BiasVarianceTradeOff_Assignment6_0805/calculatebetas.py

```
Note: The folder path conventions and other details followed are respect to Linux OS, users using Windows OS are required to change file paths and other requirements as needed for Windows OS. <br>

Output:

![biasvarianceoutput](<../Pictures/assignment6output.png>) <br>
![biasvarianceoutput](<../Pictures/biasvariance.png>) <br>
![biasvarianceoutput](<../Pictures/polynomialsdegrees1234.png>) 
