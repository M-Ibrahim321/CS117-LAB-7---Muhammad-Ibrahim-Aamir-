import numpy as np

#array 1D of 10 random integers btw 1 and 50

array=np.random.randint(1,51,size=10)

print("----------------------------------------")

print("Array",array)

#filtering EVEN and ODD Numbers and counting them

print("----------------------------------------")

even=array[array%2==0]
print("Even",even)
print(f"count of even numbers: {len(even)}")

print("----------------------------------------")

#max,min,and their indices

print("Maximum value ",np.max(array), "at Index ",np.argmax(array))
print("Minimum value ",np.min(array), "at Index ",np.argmin(array))

print("----------------------------------------")