# Program to find the length of the longest common subsequence of two sentences

# Function to find the length of the longest common subsequence of two sentences
def convolve(X, Y, m, n):
    if m == 0 or n == 0: # Base case
        return 0
    # If the last elements of the two sentences are the same
    elif X[m-1] == Y[n-1]:
        return 1 + convolve(X, Y, m-1, n-1)
    # If the last elements of the two sentences are not the same
    else: 
        return max(convolve(X, Y, m, n-1), convolve(X, Y, m-1, n))
    
# Function to split the sentences into words and call the convolve function
def splitSentence(sentence1, sentence2):
    lst1 = sentence1.split() # Split the first sentence into words
    lst2 = sentence2.split() # Split the second sentence into words
    n1 = len(lst1) # Length of the first sentence
    n2 = len(lst2) # Length of the second sentence
    return convolve(lst1, lst2, n1, n2)
    
# Main function
def main():
    sentence1 = "He is a bad boy" # First sentence
    sentence2 = "I watched bad boy" # Second sentence
    print(splitSentence(sentence1, sentence2))
    
if __name__ == "__main__":
    main()