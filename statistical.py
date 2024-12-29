import numpy as np
import statistics as stats

baked_food = [200,300,400,500,600,54,64,33,54]

a = np.array(baked_food)
print(np.mean(baked_food)) # sum of all the values /number of values
print(np.median(baked_food)) # central value after sorting
print(stats.mode(baked_food))
print(np.std(baked_food))