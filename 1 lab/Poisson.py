import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.special import factorial


lam = 10

#1-я часть
small = np.random.poisson(lam, 5)
count, bins, ignored = plt.hist(small, 30, density=True)
x = np.arange(0, 17, 1)
pdf = lam**x / factorial(x) * np.exp(-lam)

plt.plot(x, pdf)
plt.xlabel("n = 5")
plt.ylabel("density")
plt.show()

#2-я часть
med = np.random.poisson(lam, 50)
count, bins, ignored = plt.hist(med, 30, density=True)
x = np.arange(0, 19, 1)
pdf = lam**x / factorial(x) * np.exp(-lam)


plt.plot(x, pdf)
plt.xlabel("n = 50")
plt.ylabel("density")
plt.show()

#3-я часть
big = np.random.poisson(lam, 1000)
count, bins, ignored = plt.hist(big, 30, density=True)
x = np.arange(0, 23, 1)
pdf = lam**x / factorial(x) * np.exp(-lam)


plt.plot(x, pdf)
plt.xlabel("n = 1000")
plt.ylabel("density")
plt.show()
