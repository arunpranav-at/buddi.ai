import random
print("This is the program for Random Sampler")
lstsamples = input("Enter the samples: ").split()
lstin = list(map(int, input("Enter the sample frequencies: ").split()))
cnt = int(input("Enter the number of random samples: "))
lst = []
sumi = sum(lstin)
for i in lstin:
    lst.append(i/sumi)
lstcmf = [lst[0]]
for x in range(1, len(lst)):
    lstcmf.append(lst[x]+lstcmf[-1])
print("Samples Frequencies list: ", lstin)
print("Probability Mass Function (PMF) list: ", lst)
print("Cumulative Mass Function (CMF) list: ", lstcmf)
print("The random samples are: ")
for j in range(cnt):
    rf = random.uniform(0, 1)
    for k in range(len(lstcmf)):
        if rf <= lstcmf[k]:
            print(k+1, end=" ")
            print(lstsamples[k])
            break
print("Program ended. If you want to run again, please re-run the program.")