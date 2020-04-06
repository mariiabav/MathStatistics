import matplotlib.pyplot as plt
import numpy as np
import math

loc, scale = 0., 1/math.sqrt(2)


#1-я часть
small = np.random.laplace(loc, scale, 5)
count, bins, ignored = plt.hist(small, 30, density=True)
x = np.arange(-4., 4., .01)
pdf = np.exp(-abs(x-loc)/scale)/(2.*scale)

plt.plot(x, pdf)
plt.xlabel("n = 5")
plt.ylabel("density")
plt.show()

#2-я часть
med = np.random.laplace(loc, scale, 50)
count, bins, ignored = plt.hist(med, 30, density=True)
x = np.arange(-4., 4., .01)
pdf = np.exp(-abs(x-loc)/scale)/(2.*scale)

plt.plot(x, pdf)
plt.xlabel("n = 50")
plt.ylabel("density")
plt.show()

#3-я часть
big = np.random.laplace(loc, scale, 1000)
count, bins, ignored = plt.hist(big, 30, density=True)
x = np.arange(-6., 6., .01)
pdf = np.exp(-abs(x-loc)/scale)/(2.*scale)

plt.plot(x, pdf)
plt.xlabel("n = 1000")
plt.ylabel("density")
plt.show()
