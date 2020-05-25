from functools import partial
from collections import OrderedDict

import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from scipy.special import factorial


size = 20
borders = [[-4, 4]] * 4 + [[6, 14]]
bandwidths = [1/2, 1, 2]

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


def silvermans_rule(sample):
    n = sample.shape[0]
    std = np.std(sample)
    return 1.06 * std * n ** (-1 / 5)


distributions = OrderedDict(
    uniform = np.random.uniform(low, high, size),
    normal = np.random.standard_normal(size),
    poisson = np.random.poisson(lam, size),
    laplace = np.random.laplace(loc, scale, size),
    cauchy = np.random.standard_cauchy(size),
)

for idx, (name, x) in enumerate(distributions.items()):
    i = 1
    plt.suptitle(f'{name}')
    for bandwidth in bandwidths:
            ax = plt.subplot(1, 3, i)

            plt.title(f'n = {size}. H = {bandwidth}/H_n')
            x = x[(borders[idx][0] <= x) & (x <= borders[idx][1])]
            sns.kdeplot(pd.Series(x, name='KDE'), bw=bandwidth * silvermans_rule(x), ax=ax)
            
            if name == 'normal':
                x_seq = np.arange(-4., 4., .01)
                pdf = 1/math.sqrt(2*math.pi) * np.exp(-x_seq**2/2)
                plt.plot(x_seq, pdf)
                
            if name == 'cauchy':
                x_seq = np.arange(-4., 4., .01)
                pdf = 1/math.pi * 1/(x_seq**2+1)
                plt.plot(x_seq, pdf)

            if name == 'laplace':
                x_seq = np.arange(-4., 4., .01)
                pdf = np.exp(-abs(x_seq-loc)/scale)/(2.*scale)
                plt.plot(x_seq, pdf)

            if name == 'poisson':
                x_seq = np.arange(6., 14., .01)
                pdf = lam**x_seq / factorial(x_seq) * np.exp(-lam)
                plt.plot(x_seq, pdf)

            if name == 'uniform':
                x_seq = np.arange(-math.sqrt(3), math.sqrt(3), .01)
                pdf = 1/(2*math.sqrt(3))
                pdff = []
                j = 0
                while j != x_seq.size:
                    pdff.append(pdf)
                    j += 1
                plt.plot(x_seq, pdff)
            i += 1
        
    plt.show()


