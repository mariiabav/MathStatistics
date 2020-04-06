import matplotlib.pyplot as plt
import numpy as np
import math

low, high = -math.sqrt(3), math.sqrt(3)
#1-я часть
small = np.random.uniform(low, high, 5)
count, bins, ignored = plt.hist(small, 30, density=True)
x = np.arange(-math.sqrt(3), math.sqrt(3), .01)
pdf = 1/(2*math.sqrt(3))

pdff = []
i = 0
while i != x.size:
    pdff.append(pdf)
    i += 1
    
plt.plot(x, pdff)
plt.xlabel("n = 5")
plt.ylabel("density")
plt.show()

#2-я часть
med = np.random.uniform(low, high, 50)
count, bins, ignored = plt.hist(med, 30, density=True)
x = np.arange(-math.sqrt(3), math.sqrt(3), .01)
pdf = 1/(2*math.sqrt(3))

pdff = []
i = 0
while i != x.size:
    pdff.append(pdf)
    i += 1
    
plt.plot(x, pdff)
plt.xlabel("n = 50")
plt.ylabel("density")
plt.show()

#3-я часть
big = np.random.uniform(low, high, 1000)
count, bins, ignored = plt.hist(big, 30, density=True)
x = np.arange(-math.sqrt(3), math.sqrt(3), .01)
pdf = 1/(2*math.sqrt(3))

pdff = []
i = 0
while i != x.size:
    pdff.append(pdf)
    i += 1
    
plt.plot(x, pdff)
plt.xlabel("n = 1000")
plt.ylabel("density")
plt.show()
