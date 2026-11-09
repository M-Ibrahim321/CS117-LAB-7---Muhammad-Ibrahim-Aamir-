import numpy as np

#Creating the 1D arrays

array1=np.random.randint(1,50,size=5)
array2=np.random.randint(1,50,size=5)

print("array1 is ",array1)
print("----------------------------------------")
print("array2 is ",array2)
print("----------------------------------------")
#performing the operations

print("addition:",array1+array2)
print("subtraction:",array1-array2)
print("multiplication:",array1*array2)
print("division:",np.round(array1/array2,2))

print("----------------------------------------")


