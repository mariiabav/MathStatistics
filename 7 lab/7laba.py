import math
import numpy as np
import scipy.stats as st
from scipy.stats import chi2
import matplotlib.pyplot as plt
import seaborn as sns
import statistics


size = 100
k = int(1 + 3.3 * math.log(size))
alpha = 0.05


def chi_squared_test(data, mu_hat, sigma_hat):
    print("Количеcтво промежутков = ", k)
    
    a = np.linspace(-3, 3, k - 1)
    a = np.insert(a, 0, -np.inf)
    a = np.append(a, np.inf)    
    n = np.zeros(shape=(k, 1))
    for i in range(k - 1):
        for j in range(0, size):
            if a[i] < data[j] and data[j] < a[i + 1]:
                n[i] += 1


    p = np.ndarray(shape=(k, 1))
    for i in range(1, k):
        p[i - 1] = st.norm.cdf(a[i], loc=mu_hat, scale=sigma_hat) - st.norm.cdf(a[i - 1], loc=mu_hat, scale=sigma_hat)

    
    chi = np.zeros(shape=(k, 1))
    for i in range(k - 1):
        chi[i] = ((n[i] - size * p[i]) ** 2) / (size * p[i])


    
    print(" k      Interval         n_i     p_i    n_i - np_i   (n_i- np_i)^2/(np_i) ")
    for i in range(k):
        print("%2s & " % str(i + 1),
              "%5s ; " % str("%.2f" % a[i]),
              "%5s & " % str("%.2f" % a[i + 1]),
              "%3s & " % str("%.0f" % n[i]), 
              "%.5f & " % p[i],
              "%2s & " % str("%.2f" % (size * p[i])),
              "%2s & " % str("%.2f" % (n[i] - size * p[i])),
              "%.2f \\\\" % chi[i])

    print("sum &  –––––R–––––   & ",
          "%.0f & " % np.sum(n),
          "%7s & " % str("%.0f" % np.sum(p)),
          "%2s & " % str("%.0f" % np.sum(size * p)),
          "%2s & " % str("%.2f" % np.sum(n - size * p)),
          "%.2f" % np.sum(chi))
    return np.sum(chi)


def main():
    data = np.random.standard_normal(size)
    mu_hat = np.mean(data)
    sigma_hat = statistics.variance(data)
    print(mu_hat, sigma_hat)
    
    chi = chi_squared_test(data, mu_hat, sigma_hat)
    table_value = chi2.ppf(1 - alpha, k - 1)

    print(table_value) 
    if (chi < table_value):
        print('Гипотеза принимается')
    else:
        print('Гипотеза отвергается')

if __name__ == "__main__":
    main()
