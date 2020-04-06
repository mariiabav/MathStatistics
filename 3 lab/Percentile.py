import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

size = 20

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

mainOutlier = []

for number in range(1000):
    normal = np.random.standard_normal(size)
    distribution = normal
    q75 = np.percentile(distribution, 75)
    q25 = np.percentile(distribution, 25)
    iqr = q75 - q25
    cut_off = iqr * 1.5
    lower, upper = q25 - cut_off, q75 + cut_off
    outliers = [x for x in distribution if x < lower or x > upper]
    mainOutlier.append(len(outliers)/size)

print(np.percentile(mainOutlier, 50))
