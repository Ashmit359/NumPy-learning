import numpy as np

# arr = np.array([[54,8,9,7,65,54],[54,98,3,88,7655,84]])
# print(np.sort(arr))

# arr = np.array ([54,6,8,98,32])
# s = np.where(arr == 6)
# p = np.where(arr % 4 == 0)
# print(s,p)

# arr = np.array ([1,2,3,4,5,6,7,8,9])
# s = np.searchsorted(arr,5)
# print(s)

arr = np.array([20,30,40,50,60,70])


fa = [True, False,  True,  False,  True, False]

new = arr[fa]

print(new)