import numpy as np

#creating 3 by 3 matrix of random numbers btw 10 and 100
print("----------------------------------------")

matrix=np.random.randint(10,101,size=(3,3))
print("Original matrix:\n",matrix)
print("----------------------------------------")

#Replacing elements greater than 50 with 0

matrix[matrix>50]=0

print("New Matrix:\n",matrix)
print("----------------------------------------")