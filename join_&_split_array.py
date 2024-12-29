import numpy as np

# a = [4,5,6,7]
# b = [8,9,10,11]
# print(type(a))

#Concatenate
# arr1 = np.array([45,65,84])
# arr2 = np.array([54,8,55])
# print(np.concatenate([arr1,arr2]))

# arr1 = np.array([[45,65,84],[54,85,98]])
# arr2 = np.array([[54,8,55],[54,98,54]])
# print(np.concatenate([arr1,arr2], axis = 0))
# print(np.concatenate([arr1,arr2], axis = 1))
# print(np.hstack([arr1,arr2])) #horizontal concatention
# print(np.vstack([arr1,arr2])) #vertical concatention

a = np.array([4,54,6,8,2,58])
b= np.array_split(a,3)
print(b[3])