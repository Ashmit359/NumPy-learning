#np.append (h,g) -append items to an array
#np.insert (a, 1, 5) -inserta items in an array
#np.delete (a, [1]) - delete items from an array

import numpy as np 

# a = np.array([[45,65],[54,55]])
# print(np.append(a,[90,78]))

# np.insert

# a = np.array([[55,64],[55,7],[88,86]])
# print(np.insert(a,2,777)) #array, index, value
# print(np.insert(a,1,[45,65], axis = 0))

# np.delete

a = np.array([565,85,86,89])
print(np.delete(a,[1]))