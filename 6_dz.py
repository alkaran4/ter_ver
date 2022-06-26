import numpy as np

# 1

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

cov_1 = np.mean(zp * ks) - np.mean(zp) * np.mean(ks) # 9157.83999
cov_2 = np.cov(zp, ks, ddof=0) # 9157.84

std_zp = np.std(zp)
std_ks = np.std(ks)

cor_1 = cov_1 / (std_zp * std_ks) # 0.8875
cor_2 = np.corrcoef(zp, ks) # 0.8875

# 2

IQ = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
alfa = 0.05

# Так как неизвестна стандартное отклоение генерального совокупности, используем критерий Стьюдента.

def invl(M, Z, sig, n):
    x = Z * sig / n**0.5
    return [round(M - x, 3), round(M + x, 3)]

print(invl(np.mean(IQ), 2.262, np.std(IQ, ddof=1), 10)) #[110.557, 125.643]

# 3

sig = 5
n = 27
mu = 174.2
alfa = 0.05

print(invl(mu, 1.96, sig, n)) # [172.314, 176.086]

# 4
# EDA

