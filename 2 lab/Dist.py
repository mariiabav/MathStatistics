import matplotlib.pyplot as plt
import numpy as np
import math


n = 1000
#array = np.random.standard_cauchy(n)

numOfCalculations = 1000

averageSeq = []
medSeq = []
z_rSeq = []
z_qSeq = []
z_trSeq = []

def findZ(n): #5 массивов, в каждом 1000 соотв элементов. 1 элемент - для 1 выборки
    i = 0;
    low, high = -1/math.sqrt(3), 1/math.sqrt(3),
    while i < numOfCalculations:
        array = np.random.uniform(low, high, n)
        averageSeq.append(findAv(array, n))
        medSeq.append(findMed(array, n))
        z_rSeq.append(findZ_R(array, n))
        z_qSeq.append(findZ_Q(array, n))
        z_trSeq.append(findZ_tr(array, n))
        i += 1;

def findE(averageSeq, medSeq, z_rSeq, z_qSeq, z_trSeq):
    result = []
    result.append(findAv(averageSeq,numOfCalculations))
    result.append(findAv(medSeq,numOfCalculations))
    result.append(findAv(z_rSeq,numOfCalculations))
    result.append(findAv(z_qSeq,numOfCalculations))
    result.append(findAv(z_trSeq,numOfCalculations))
    return result
#[av, med, z_r, z_q, z_tr]

def findD(averageSeq, medSeq, z_rSeq, z_qSeq, z_trSeq):
    result = []
    i = 0
    average2Seq = []
    med2Seq = []
    z_r2Seq = []
    z_q2Seq = []
    z_tr2Seq = []
    for element in averageSeq:
        average2Seq.append(element**2)
        
    for element in medSeq:
        med2Seq.append(element**2)
        
    for element in z_rSeq:
        z_r2Seq.append(element**2)
        
    for element in z_qSeq:
        z_q2Seq.append(element**2)
        
    for element in z_trSeq:
        z_tr2Seq.append(element**2)
    
    z2 = findE(average2Seq, med2Seq, z_r2Seq, z_q2Seq, z_tr2Seq)
    z = findE(averageSeq, medSeq, z_rSeq, z_qSeq, z_trSeq)
    while i < len(z2):
        result.append(z2[i] - z[i]**2)
        i += 1;
    return result
        
    
def findAv(array, n):
    return 1/n * np.sum(array)

    
def findMed(array, n):
    l = int(n/2)
    if n % 2 == 0:
        return (array[l]+array[l-1])/2
    else:
        return small[l]

    
def findZ_R(array, n):
    return (array[0] + array[n - 1])/2


def findQuartile(p, array, n):
    if (n*p).is_integer() == True:
        return array[int(n*p-1)]
    else:
        return array[int(n*p)]
    
def findZ_Q(array, n):
    p1 = 1/4
    p2 = 3/4
    return (findQuartile(p1, array, n) + findQuartile(p2, array, n))/2
    
def findZ_tr(array, n):
    r = n/4
    lowerBound = math.ceil(r) #округление до верхнего знака
    upperBound = math.floor(n-r-1) #округление до нижнего знака
    sliceArray = array[lowerBound:upperBound]
    return 1/(n-2*r) * sliceArray.sum()

def findDispSum(array, n):
    average = findAv(array, n)
    sum = 0
    for element in array:
        sum += (element-average) ** 2
    return sum
        
def findDispersion(array, n):
    return 1/n*findDispSum(array, n)



findZ(n) #заполняем массивы последовательностей 5-ти характеристик
E = findE(averageSeq, medSeq, z_rSeq, z_qSeq, z_trSeq) #считаем E из каждой последовательности
D = findD(averageSeq, medSeq, z_rSeq, z_qSeq, z_trSeq)
#print(E)
#print(D)

#poisson(), 
low, high = 0, 1/math.sqrt(2);
array = np.random.standard_cauchy(1000)
#array = np.random.poisson(1000)
print(findAv(array, n), "&", findMed(array, n), "&",findZ_R(array, n), "&",findZ_Q(array, n), "&",findZ_tr(array, n))




