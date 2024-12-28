#g=a-b
# np.subtract (a, b)
# b+an
# p.add (b, a)
# a/ b
# np.divide(a,b)
# a*b
# np.multiply (a, b)
# np.exp(b)
# np.sqrt(b)
# np.pow(a)

import numpy as np 

arr1 = np.array ([[30,54],[55,85]])
arr2 = np.array ([[54,88],[64,41]])
print (arr1 + arr2)
print (np.add(arr1,arr2))

arr1 = np.array ([[30,54],[55,85]])
arr2 = np.array ([[54,88],[64,41]])
print (arr1 - arr2)
print (np.subtract (arr1,arr2))

arr1 = np.array ([[30,54],[55,85]])
arr2 = np.array ([[54,88],[64,41]])
print (arr1 / arr2)
print (np.divide (arr1,arr2))

arr1 = np.array ([[30,54],[55,85]])
arr2 = np.array ([[54,88],[64,41]])
print (arr1 * arr2)
print (np.multiply (arr1,arr2))

arr1 = np.array ([[30,54],[55,85]])
print (np.exp(arr1) )

arr1 = np.array ([[3,4],[5,6]])
print (np.sqrt(arr1) )
