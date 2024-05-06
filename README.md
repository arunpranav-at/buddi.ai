# buddi.ai
Daily assignments and related documentations along with code will be updated here

## Assignment 1 - 02/05/2024
Problem statement: Input values = [-3, -2, -1, 0, 1, 2, 3] and the corresponding Output values = [7, 2, 0, 0, 0, 2, 7]. Our aim is to find a polynomial function of degree 2 of the format b1*x + b2*x^2 would result in output values if x values are the corresponding input values.<br><br>

Solution: We are supposed to form find values of b1 (beta1) and b2 (beta2) such that the Error E (epsilon) value which is the sum of absolute difference for all inputs together is minimum. We are taking the interval of -1 to 1 in intervals 0.001 for both b1 and b2.<br><br>

Code: Refer newfunctionfind0605.py in Assignment1_0205 folder <br><br>
To install required libraries:
```
pip install matplotlib, mpl_toolkits, numpy
```
Move into the Assignment1_0205 Directory
```
cd Assignment1_0205/
```
Run the python file with the below code
```
python3 newfunctionfind0605.py
```
Note: The folder path conventions and other details followed are respect to Linux OS, users using Windows OS are required to change file paths and other requirements as needed for Windows OS <br><br>

Output: We are finding lowest E (epsilon) value and its corresponding b1 (beta1) and b2 (beta2) values. We are plotting the surface plot for the same.<br>

![minmax b1 b2 values](<Pictures/Screenshot from 2024-05-06 23-17-49.png>) <br><br>
![surface plot output](<Pictures/Screenshot from 2024-05-06 23-17-23.png>)

## Assignment 2 - 06/05/2024



