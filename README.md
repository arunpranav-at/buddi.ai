# buddi.ai
Daily assignments and related documentations along with code will be updated here

## Assignment 1 - 02/05/2024
Problem statement: Input values = [-3, -2, -1, 0, 1, 2, 3] and the corresponding Output values = [7, 2, 0, 0, 0, 2, 7]. Our aim is to find a polynomial function of degree 2 of the format b1*x + b2*x^2 would result in output values if x values are the corresponding input values.<br>

Solution: We are supposed to form find values of b1 (beta1) and b2 (beta2) such that the Error E (epsilon) value which is the sum of absolute difference for all inputs together is minimum. We are taking the interval of -1 to 1 in intervals 0.001 for both b1 and b2.<br>

Code: Refer newfunctionfind0605.py in Assignment1_0205 folder <br>
To install required libraries:
```
pip install matplotlib, mpl_toolkits, numpy
```
Move into the Assignment1_0205 Directory
```
cd Assignment1_0205/
```
Run the python file
```
python3 newfunctionfind0605.py
```
Note: The folder path conventions and other details followed are respect to Linux OS, users using Windows OS are required to change file paths and other requirements as needed for Windows OS. <br>

Output: We are finding lowest E (epsilon) value and its corresponding b1 (beta1) and b2 (beta2) values. We are plotting the surface plot for the same.<br>

![minmax b1 b2 values](<Pictures/assign1output.png>) <br>
![surface plot output](<Pictures/surfaceplot.png>)

## Assignment 2 - 06/05/2024
Problem statement: We are trying to estimate the value of PI using Monty Carlo Simulation <br>

Monty Carlo Simulation: Monte Carlo simulation is a mathematical technique that uses repeated random sampling to predict he likelihood of possible outcomes for an uncertain event. It's also known as the Monte Carlo Method or multiple probability simulation. <br>

Solution: Monte Carlo simulation is a statistical technique that can be used to estimate the value of pi with high accuracy. The method involves generating a large number of random points within a square and counting the number of points that fall inside a circle inscribed in the square. The probability of a point falling inside the circle is proportional to the area of the circle, which is pi. <br>

Formula: Value of PI = 4 * ((number of darts fell inside circle) / (number of total darts thrown)). This formula is derived by finding the probablity of dart falling inside circle which is the area of circle divided by the area of square. It is PI*r^2/a^2 where a is the side of the square and r is the radius of the circle. Here r = a/2 as diameter is a when circle is inscribed inside the square. We are taking unit square in this case<br>

Code: To generate random points, we have used two methods - Uniform Random Samples using random.uniform() function and Normal Samples using random.normal(). <br>
Please refer pivalueusinguniform.py in Assignment2_0605 folder for simulation using Uniform Random Samples<br>
Please refer pivalueusingnormal.py in Assignment2_0605 folder for simulation using Normal Samples<br>

To install required libraries:
```
pip install matplotlib, mpl_toolkits, numpy, math, random
```
Move into the Assignment1_0205 Directory
```
cd Assignment2_0605/
```
Run the python files
```
python3 pivalueusinguniform.py
```
```
python3 pivalueusingnormal.py
```
Note: The folder path conventions and other details followed are respect to Linux OS, users using Windows OS are required to change file paths and other requirements as needed for Windows OS. <br>

Output: We can understand that more the number of darts thrown, the estimated value of PI gets closer to the actual value of PI. <br>

![montycarlosimulationoutput](<Pictures/montycarlospisimulation.png>)<br><br><br>

![outputusinguniformrandomsamples](<Pictures/outputuniformpi.png>)<br>
![graphusinguniformrandomsamples](<Pictures/pivalueusinguniformrandomsamples.png>)<br><br>

![outputusingnormalsamples](<Pictures/outputfornormalsamples.png>)<br>
![graphusingnormalsamples](<Pictures/graphfornormalsamples.png>)<br>

Note: As these are randomly generated, for every experiment the plotted graph and values generated changes.

## Assignment 3 - 07/05/2024
Problem statement: Build a random sampler which takes in list of frequencies for samples and along with the number of samples to be selected randomly. Use Uniform Random Function generator for this purpose. <br>

Solution: I have provided two programs, one is function based random sampler - functionalrandomsampler.py where I have implemented a randomsampler function which satisfies the definition of 
```
def randomsampler(sampledict: dict[str: float], cnt: int) -> list[str]:
```
and another program randomsampler.py which is an user interactive program. <br>
We will use python random module's uniform function random.uniform() to generate a floating value between 0 and 1. The input list will be consisting of frequencies. We will first find the Probability Mass Functions (PMF) list for each frequency in the list. Then we will find the corresponding Cumulative Probability Functions (CMF) list. Then the randomly generated float value from random.uniform() is compared (greater than) each time to print the random sample <br>

Code: Please refer randomsampler.py and functionalrandomsampler.py in Assignment3_0705<br>
To install required libraries:
```
pip install random
```
Move into the Assignment3_0705 Directory
```
cd Assignment3_0705/
```
Run the python file as per your requirement
```
python3 functionalrandomsampler.py
```
```
python3 randomsampler.py
```
Note: The folder path conventions and other details followed are respect to Linux OS, users using Windows OS are required to change file paths and other requirements as needed for Windows OS. <br>

Output: The index of the input frequencies (one based indexing) is printed along with the sample randomly for n number of times where n is the number of random samples given in input by the user during program execution.<br>

For functionalrandomsampler.py, output generated one time was: 
```
['qrst', 'ijkl', 'mnop', 'mnop', 'qrst', 'mnop', 'abcd', 'efgh', 'mnop', 'uvwxyz']
```
and randomsampler.py generated output once like this:
![assignment3](<Pictures/assignment3.png>)<br>
