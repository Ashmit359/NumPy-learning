#Function
# a.shape - Array dimensions
# len(a) - Length of array
# b.ndim - Number of array dimensions
# e.size - Number of array elements
# b.dtype - Data type of array elements
# b.astype(int) - Convert on array to a different type

import numpy as np 

a = [30,40,20,40,30]
arr = np.array(a)
print (arr)
print (arr.shape) #row, columns
print (len(arr))  #number of nested values
print (np.size(arr)) #number of elements
print (type(arr)) #datatype of variable
print (arr.dtype) #data type of array 
print (arr.astype(float)) # conversion of dattype 

#-----------------------------------------------------------------------------------------

#chatgpt provide note according to my code 
# Notes for NumPy Functions and Code Example

# Functions Overview
# - a.shape: Returns the dimensions (rows and columns) of the array.
# - len(a): Gives the length of the array (number of elements in the outermost dimension).
# - b.ndim: Provides the number of dimensions in the array.
# - e.size: Returns the total number of elements in the array.
# - b.dtype: Specifies the data type of the array elements (e.g., int32, float64).
# - b.astype(int): Converts the data type of the array to a specified type (e.g., int, float).

# Code Example with Explanations
import numpy as np 

# Step 1: Define a Python list
# 'a' is a simple Python list containing integers.
a = [30, 40, 20, 40, 30]

# Step 2: Convert the list to a NumPy array
# The list is converted to a NumPy array using np.array().
arr = np.array(a)

# Step 3: Print the NumPy array
# The array is displayed to show how the list looks after conversion.
print(arr)  # Output: [30 40 20 40 30]

# Step 4: Get the shape of the array
# arr.shape provides the dimensions of the array. For a 1D array, it returns (number of elements,).
print(arr.shape)  # Output: (5,)

# Step 5: Find the length of the array
# len(arr) gives the number of elements in the array. For 1D arrays, it's the same as the total number of elements.
print(len(arr))  # Output: 5

# Step 6: Get the total number of elements
# np.size(arr) provides the total count of elements in the array. Useful for multi-dimensional arrays.
print(np.size(arr))  # Output: 5

# Step 7: Display the type of the array variable
# type(arr) shows the data type of the variable. Here, it's a NumPy ndarray.
print(type(arr))  # Output: <class 'numpy.ndarray'>

# Step 8: Check the data type of array elements
# arr.dtype shows the data type of the elements stored in the array.
print(arr.dtype)  # Output: int64 (may vary based on your system)

# Step 9: Convert the array data type to float
# arr.astype(float) converts the elements of the array to float type.
print(arr.astype(float))  # Output: [30. 40. 20. 40. 30.]

# Summary
# - This code demonstrates basic array operations in NumPy.
# - Key functions include shape, length, size, type, and type conversion.
# - Useful for understanding array properties and how to manipulate data.