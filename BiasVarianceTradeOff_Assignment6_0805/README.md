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
python3 BiasVarianceTradeOff_Assignment6_0805/combined.py
python3 BiasVarianceTradeOff_Assignment6_0805/numpybiasvariancetradeoff.py
python3 BiasVarianceTradeOff_Assignment6_0805/calculatebetas.py
python3 BiasVarianceTradeOff_Assignment6_0805/lagrangelinebiasvariance.py

```
Why 4 files? You might think! Each file has it's own speciality <br>
combined.py - this is the proper program which does every work without the help of Polynomial builtin functions <br>
lagrangelinebiasvariance.py - this program plots lagrange line for the selected points and also calculates variance and bias for the lagrange points <br>
numpybiasvariancetradeoff.py - this program uses Polynomial builtin functions to complete all work. This is the most easiest program for me to create <br>
calculatebetas.py - this program plots Polynomial functions without builtin Polynomial functions but uses builtin functions for plotting variance and bias <br><br>

Note: The folder path conventions and other details followed are respect to Linux OS, users using Windows OS are required to change file paths and other requirements as needed for Windows OS. <br>

Output:

![biasvarianceoutput](<../Pictures/assignment6output.png>) <br>
![biasvarianceoutput](<../Pictures/biasvariance.png>) <br>
![biasvarianceoutput](<../Pictures/polynomialsdegrees1234.png>) 
