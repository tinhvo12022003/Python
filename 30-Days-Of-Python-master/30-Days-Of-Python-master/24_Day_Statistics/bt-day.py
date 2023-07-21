import numpy as np
import statistics as st
import matplotlib.pyplot as plt
import string

#create int numpy arrays
python_list = [1, 2, 3, 4] #print(type(python_list)) #<class 'list'>

two_dimensional_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(two_dimensional_list) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

numpy_array_from_list = np.array(python_list) 
print(numpy_array_from_list) # [1, 2, 3, 4]


#create float numpy arrays
python_float_numpy_array = np.array(python_list, dtype=float)
print(python_float_numpy_array) # [1., 2., 3., 4.] 

#crate bool numpy arrays
python_bool_numpy_array = np.array(python_list, dtype=bool)
print(python_bool_numpy_array) # [True, True, True, True]

#create multidimensional numpy array using numpy
two_dimensional_list_numpy_array = np.array(two_dimensional_list)
print(two_dimensional_list_numpy_array) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#converting numpy arra6 to list
np_to_list = python_float_numpy_array.tolist()

#creating numpy to tuple
python_tuple = (1, 2, 3, 4, 5)
numpy_array_from_tuple = np.array(python_tuple)
print(numpy_array_from_tuple) # [1, 2, 3, 4, 5]


#shape of numpy array
print(two_dimensional_list_numpy_array.shape) # (3, 3)
print(numpy_array_from_tuple.shape)

#data type of number array
int_list = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_list)
float_list = np.array(int_list, dtype=float)
print(int_array)
print(int_array.dtype)
print(float_list)
print(float_list.dtype)

#size of a number array
print(int_array.size)
print(float_list.size)


#ADDITION
list1 = np.array([1, 2, 3, 4, 5], dtype=int)
list2 = np.array([6, 7, 8, 9, 10], dtype=int)
print(list1 + list2)
print(list1 + list2 + 1)

#SUBTRACTION
print(list1 - list2)
print(list1 - 10)

#MULTIPLICATION
print(list1 * list2)
print(list1 * 10)


#DIVISION
print(list1 / list2)
print(list1 / 2)

#MODULUS
print(list1 % list2)


#FLOOR DIVISION
print(list1 // 2)

#EXPONENT
print(list1 ** 2)

#MULTIDEMENSIONAL ARRAYS
mul_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(mul_array))
print(mul_array.shape)

#getting items from numpy array
first_row = mul_array[0]
second_row = mul_array[1]
third_row = mul_array[2]

first_column = mul_array[:, 0]
second_column = mul_array[:, 1]
third_column = mul_array[:, 2]

print(first_row, second_row, third_row)
print(first_column, second_column, third_column)

print(mul_array[:2, :3])

#Slicing numpy array
print(mul_array[::])  # all rows
two_row_two_col = mul_array[:2, :2]
print(two_row_two_col)

#reverse the row and column
    #-->reverse row  , -->reverse column  
print(mul_array[::-1, ::-1])
print(mul_array[:3:2, :3:2])
print(mul_array[1:3:2, 1:3:2])

#change value in numpy array
mul_array[1, 1] = 100
print(mul_array)

#numpy zeros
zeros_array = np.zeros((3, 3), dtype=int, order='C')
print(zeros_array)

ones_array = np.ones((2, 3), dtype=int, order='C')
print(ones_array)

first_shape = mul_array.shape
print(first_shape)

list3 = np.array([[1, 2, 3], [4, 5, 6]])
first_reshape = list3.reshape(3, 2)
print(first_reshape.flatten())

hstack = np.hstack((list1, list2), dtype=int, casting='same_kind')
print(hstack)

vstack = np.vstack((list1, list2), dtype=int, casting='same_kind')
print(vstack)

arr = np.random.randint(10, 100, size=100)
print(arr)

#create int list random
int_random_list =  np.random.randint(3, 10, size=9)
print(int_random_list)

#create float list random
float_random_list = np.random.rand(9)
print(float_random_list)

#create multidimensional list random
multidimensional_random_list = np.random.randint(0, 10, size=(3, 3))
print(multidimensional_random_list)

import seaborn as sns
normal_array = np.random.normal(79, 15, 80)
# print(normal_array)

# sns.set()
# plt.hist(normal_array)
# plt.show()

#Arange
lst = range(0, 11, 1)
# for i in lst:
#     print(i)

whole_numbers = np.arange(0, 20, 1)  #start, end, step
print(whole_numbers)

linspace = np.linspace(1, 20, 20, dtype=int) #start end size dtype
print(linspace)

logspace = np.logspace(1, 4, 20, dtype=int)
print(logspace) #same linspace but log(10)


a = [1, 2, 3]
tile = np.tile(a, 3)
repeat = np.repeat(a, 3)
print(tile) #loop array n times
print(repeat) #repeat each element n times

print("".join(np.random.choice(list((string.ascii_letters + string.digits)), size=10)))


f = np.array([1, 2, 3])
g = np.array([4, 5, 6])
print(np.dot(f, g))

h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
np.matmul(h, i)