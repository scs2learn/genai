import numpy as np

my_array = np.array([[1,2,3], [4,5,6], [7,8,9]])

#print the array
print(my_array)

#print the shape of the array
print(my_array.shape)

#print the datatype of the array
print(my_array.dtype)

#perform some basic arithematic on the array
result = my_array + 2
print(result)

#calculate the mean of the array
mean = np.mean(my_array)
print(mean)
