import numpy as np
from matplotlib import pyplot as plt

# 1

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])


b = (np.mean(zp * ks) - np.mean(zp) * np.mean(ks)) / (np.mean(zp**2) - (np.mean(zp))**2) # 2.62
a = np.mean(ks) - b * np.mean(zp) # 444.18


# plt.scatter(zp, ks)
# plt.plot(zp, a + b*zp)
# plt.show()

# 2

zp = zp.reshape((10,1))
ks = ks.reshape((10,1))

# zp = np.hstack([np.ones((10,1)), zp])
b = np.linalg.inv(zp.T@zp)@zp.T@ks # 2.62
# a = 444.178

# 3

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

def mse_(B0, B1, x=zp, y=ks, n=10):
    return np.sum((B0 + B1*x - y)**2)/n

B0 = 0.1
B1 = 0.1
alpha = 10**(-4)
n = 10

for i in range(3000000):
    B0 -= alpha * (2/n) * np.sum(B0 + B1*zp - ks)
    B1 -= alpha * (2/n) * np.sum((B0 + B1*zp - ks) * zp)
    if i%100000 == 0:
        print(f'iteration: i={i}, B0={B0}, B1={B1}, mse={mse_(B0, B1)}')

# B0 = 444.17717616381617
# B1 = 2.62070411470
