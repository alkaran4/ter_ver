import numpy as np



# 1

sig = 16
Z = 1.96
M = 80
n = 256

def invl(sig,Z, M, n):
    x = Z * sig / n**0.5
    return [round(M - x, 3), round(M + x, 3)]

print(invl(sig, Z, M, n))

# 2

n = 10
results = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
t = 2.262
M = results.mean()
print(invl(np.std(results), t, M, n))

# 3

mu = 17
mu_0 = 17.5
alfa = 0.05
n = 100
dis = 4
Z = 1.645

Z_n = (17.5 - 17) / (dis ** 0.5 / n ** 0.5)
print(round(Z_n, 5)) # 2.5
# Отвергаем H_0, так как Z1 больше, чем Z0

# 4

M = 200
results = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
n = 10
t = 3.25

t_n = (np.mean(results) - M) / (np.std(results, ddof=1) / n ** 0.5)
print(t_n)

# Принимаем H0, так как нет статистически значимх различий