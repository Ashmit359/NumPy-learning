import numpy as np

arr = np.array([20,30,40,50,60])
print(np.sum(arr))
print(np.max(arr))
print(np.min(arr))
print(np.size(arr))
print(np.mean(arr))
print(np.cumsum(arr))
print(np.cumprod(arr))

a = [10,20,30,40]
b = [50,60,70,80]
price = np.array(a)
quantity = np.array(b)

print(price, "\n", quantity)
print()
c = np.cumprod([price,quantity], axis=0)
print(c[1].sum())