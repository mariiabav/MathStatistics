import matplotlib.pyplot as plt
import numpy as np
import math

#1-я часть
small = np.random.standard_cauchy(5)
count, bins, ignored = plt.hist(small, 30, density=True)
x = np.arange(-4., 4., .01)
pdf = 1/math.pi * 1/(x**2+1)

plt.plot(x, pdf)
plt.xlabel("n = 5")
plt.ylabel("density")
plt.show()

#2-я часть
med = np.random.standard_cauchy(50)
count, bins, ignored = plt.hist(med, 30, density=True)
x = np.arange(-4., 4., .01)
pdf = 1/math.pi * 1/(x**2+1)


plt.plot(x, pdf)
plt.xlabel("n = 50")
plt.ylabel("density")
plt.show()

#3-я часть
big = np.random.standard_cauchy(1000)
count, bins, ignored = plt.hist(big, 30, density=True)
x = np.arange(-6., 6., .01)
pdf = 1/math.pi * 1/(x**2+1)


plt.plot(x, pdf)
plt.xlabel("n = 1000")
plt.ylabel("density")
plt.show()


#3-я часть
data = np.random.standard_cauchy(1000)

count, bins, ignored =  plt.hist(data, density=True, bins=30) 
plt.xlim (-50, -40)
plt.xlabel("Приближение участка исходного графика")
plt.show()
