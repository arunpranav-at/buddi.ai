# Implement Least Common Subsequence - Assignment 11 - 21/05/2024

#### `convolve(X, Y, m, n)`
A recursive function that calculates the length of the longest common subsequence (LCS) between two lists of words using a convolution-like approach.

**Parameters:**
- `X` (list of str): The first list of words.
- `Y` (list of str): The second list of words.
- `m` (int): The length of the first list of words.
- `n` (int): The length of the second list of words.

**Returns:**
- `int`: The length of the longest common subsequence between the two lists of words.

**Description:**
The function checks the base case where either of the lists is of length zero, in which case the LCS length is zero. If the last elements of the two lists are equal, it adds one to the LCS length and recursively calls itself with the lengths of the lists decreased by one. If the last elements are not equal, it recursively calls itself twice, once with the length of the first list decreased by one and once with the length of the second list decreased by one, and returns the maximum of these two calls.

#### `splitSentence(sentence1, sentence2)`
A function that splits two sentences into lists of words and calculates the length of their longest common subsequence using the `convolve` function.

**Parameters:**
- `sentence1` (str): The first sentence.
- `sentence2` (str): The second sentence.

**Returns:**
- `int`: The length of the longest common subsequence of words between the two sentences.

**Description:**
The function splits the input sentences into lists of words using the `split()` method. It then determines the lengths of these lists and calls the `convolve` function to calculate the LCS length.

#### `main()`
The main function that serves as the entry point for the script. It demonstrates the use of the `splitSentence` function by passing two example sentences and printing the length of their longest common subsequence.

**Description:**
The `main` function defines two example sentences and calls the `splitSentence` function with these sentences. It prints the length of the LCS of words between the two sentences.

#### Example Usage
```python
def main():
    sentence1 = "He is a bad boy"
    sentence2 = "I watched bad boy"
    print(splitSentence(sentence1, sentence2))

if __name__ == "__main__":
    main()
```

**Output:**
```
2
```

**Explanation:**
For the example sentences "He is a bad boy" and "I watched bad boy", the longest common subsequence of words is "bad boy", which has a length of 2.

### Summary
This script defines a recursive approach to find the longest common subsequence (LCS) of words between two sentences by splitting the sentences into lists of words and applying a convolution-like method. The `convolve` function implements the recursive LCS logic, and the `splitSentence` function prepares the sentences for this calculation. The `main` function demonstrates the usage of these functions with an example.

Code: Refer ConvolveOneDimensionStringArrays_Assignment11_2105/convolveforstrings.py <br>

Run the python file directly without entering into the directory using the below code
```
python3 ConvolveOneDimensionStringArrays_Assignment11_2105/convolveforstrings.py
```
Note: The folder path conventions and other details followed are respect to Linux OS, users using Windows OS are required to change file paths and other requirements as needed for Windows OS. <br>