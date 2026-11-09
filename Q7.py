import numpy as np

#creating 4 by 4 matrix with random integers btw 1 and 100

matrix=np.random.randint(1,101,size=(4,4))

print("Original Matrix : ",matrix)

#Calculations

print("\nSum of All Elements : ",np.sum(matrix))
print("\nMean of All Elements : ",np.mean(matrix))
print("\nStandard Deviation of All Elements : ",np.std(matrix))


#Reshaping the matrix into 2 by 8

reshape=matrix.reshape(2,8)
print("\nReshaped Matrix 2 by 8 :\n ",reshape)