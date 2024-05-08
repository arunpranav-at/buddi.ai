# Monty Carlo PI Value Estimation - Assignment 2 - 06/05/2024
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

![montycarlosimulationoutput](<../Pictures/montycarlospisimulation.png>)<br><br><br>

![outputusinguniformrandomsamples](<../Pictures/outputuniformpi.png>)<br>
![graphusinguniformrandomsamples](<../Pictures/pivalueusinguniformrandomsamples.png>)<br><br>

![outputusingnormalsamples](<../Pictures/outputfornormalsamples.png>)<br>
![graphusingnormalsamples](<../Pictures/graphfornormalsamples.png>)<br>

Note: As these are randomly generated, for every experiment the plotted graph and values generated changes.

