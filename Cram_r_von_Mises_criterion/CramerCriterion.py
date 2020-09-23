import math
import numpy as np
import random
import scipy.stats as st
import statistics


size = 50

def cramer_von_mises_criterion(data, mu_hat, sigma_hat):

    A = np.zeros(shape=(size, 1))
    B = np.zeros(shape=(size, 1))
    C = np.zeros(shape=(size, 1))
    D = np.zeros(shape=(size, 1))
    E = np.zeros(shape=(size, 1))
    F = np.zeros(shape=(size, 1))
    G = np.zeros(shape=(size, 1))
    H = np.zeros(shape=(size, 1))
    I = np.zeros(shape=(size, 1))

    
    for j in range(size):
        A[j] = (2 * j + 1)/(2 * size) 
        
    for j in range(size):
        B[j] = st.norm.cdf(data[j], loc=mu_hat, scale=sigma_hat)

    for j in range(size):
        C[j] = math.log(B[j])

    for j in range(size):
        D[j] = A[j] * C[j]

    for j in range(size):
        E[j] = 1 - A[j]

    for j in range(size):
        F[j] = 1 - B[j]

    for j in range(size):
        G[j] = math.log(F[j])

    for j in range(size):
        H[j] = E[j] * G[j]

    for j in range(size):
        I[j] = D[j] + H[j]

    ISum = np.sum(I)
    print("Сумма значений 10го столбца таблицы: %.6f" + str(ISum))
    nomega2 = -size - 2*ISum
    

    print(" j      A          B          C           D            E           F          G          H         I")
    for j in range(size):
        print("%2s | " % str(j + 1), 
              "%s | " % str("%.3f" % A[j]),
              "%s | " % str("%.6f" % B[j]),
              "%s | " % str("%.5f" % C[j]),
              "%s | " % str("%.5f" % D[j]),
              "%s | " % str("%.4f" % E[j]),
              "%s | " % str("%.6f" % F[j]),
              "%s | " % str("%.5f" % G[j]),
              "%s | " % str("%.5f" % H[j]),
              "%s | " % str("%.5f" % I[j])
              )

    return nomega2


def main():
    data = np.random.standard_normal(size)
    #data = [15.61, 20.71, 21.68, 22.28, 23.22, 24.14, 24.59, 26.18, 26.23, 27.59, 27.88, 28.74, 29.34, 30.86, 32.08]
    data = np.sort(data)
    mu_hat = np.mean(data) 
    sigma_hat = math.sqrt(statistics.variance(data))
    print("Значения параметров нормального распределения согласно методу м. п.") 
    print(str("%.4f" % mu_hat), str("%.4f" % sigma_hat))

    x = cramer_von_mises_criterion(data, mu_hat, sigma_hat)
    print("Значение статистики:" + str(x))

    
if __name__ == "__main__":
    main()
