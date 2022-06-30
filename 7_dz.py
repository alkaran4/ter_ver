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
b = np.linalg.inv(zp.T@zp)@zp.T@ks
print(b)

# 3