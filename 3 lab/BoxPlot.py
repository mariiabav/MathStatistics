import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

size = 100

#Равномерное
low, high = -math.sqrt(3), math.sqrt(3)
uniform = np.random.uniform(low, high, size)

#Нормальное
normal = np.random.standard_normal(size)

#Пуассона
lam = 10
poisson = np.random.poisson(lam, size)

#Лапласа
loc, scale = 0.0, 1/math.sqrt(2)
laplace = np.random.laplace(loc, scale, size)

#Коши
cauchy = np.random.standard_cauchy(size)


my_dict = {'C': cauchy, 'N': normal, 'P': poisson, 'L': laplace, 'U': uniform }

fig, ax = plt.subplots()
ax.boxplot(my_dict.values())
ax.set_xticklabels(my_dict.keys())
plt.ylabel("n = 100")
plt.show()
plt.show()


