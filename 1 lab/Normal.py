import matplotlib.pyplot as plt
import numpy as np
import math

#1-я часть
small = np.random.standard_normal(5)
count, bins, ignored = plt.hist(small, 30, density=True)
x = np.arange(-4., 4., .01)
pdf = 1/math.sqrt(2*math.pi) * np.exp(-x**2/2)

plt.plot(x, pdf)
plt.xlabel("n = 5")
plt.ylabel("density")
plt.show()

#2-я часть
med = np.random.standard_normal(50)
count, bins, ignored = plt.hist(med, 30, density=True)
x = np.arange(-4., 4., .01)
pdf = 1/math.sqrt(2*math.pi) * np.exp(-x**2/2)

plt.plot(x, pdf)
plt.xlabel("n = 50")
plt.ylabel("density")
plt.show()

#3-я часть
big = np.random.standard_normal(1000)
count, bins, ignored = plt.hist(big, 30, density=True)
x = np.arange(-6., 6., .01)
pdf = 1/math.sqrt(2*math.pi) * np.exp(-x**2/2)
plt.plot(x, pdf)
plt.xlabel("n = 1000")
plt.ylabel("density")
plt.show()
