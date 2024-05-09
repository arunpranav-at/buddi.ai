# Random Sampler - Assignment 3 - 07/05/2024
Problem statement: Build a random sampler which takes in list of frequencies for samples and along with the number of samples to be selected randomly. Use Uniform Random Function generator for this purpose. <br>

Solution: I have provided two programs, one is function based random sampler - functionalrandomsampler.py where I have implemented a randomsampler function which satisfies the definition of 
```
def drawSamples(pmfdict: dict[str: float], n: int) -> list[str]:
```
and another program randomsampler.py which is an user interactive program. <br>
We will use python random module's uniform function random.uniform() to generate a floating value between 0 and 1. The input list will be consisting of frequencies. We will first find the Probability Mass Functions (PMF) list for each frequency in the list. Then we will find the corresponding Cumulative Probability Functions (CMF) list. Then the randomly generated float value from random.uniform() is compared (greater than) each time to print the random sample <br>

Code: Please refer randomsampler.py and functionalrandomsampler.py in RandomSampler_Assignment3_0705<br>
To install required libraries:
```
pip install random
```
Move into the RandomSampler_Assignment3_07055 Directory
```
cd RandomSampler_Assignment3_0705/
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
![assignment3](<../Pictures/assignment3.png>)<br>
