import numpy as np


fb = [173, 175, 180, 178, 177, 185, 183, 182] # футболисты
hc = [177, 179, 180, 188, 177, 172, 171, 184, 180] # хоккеисты
wl = [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170] # штангисты
k = 3
n = len(fb) + len(hc) + len(wl) # 28


Y_ = np.mean(fb + hc + wl)


def S_2(*args):
    result = 0
    for num in args:
        result += sum((num - Y_)**2)
    return result


def S_2_F(*args):
    result = 0
    for i in args:
        result += ((np.mean(i) - Y_)**2) * len(i)
    return result


def S_2_REM(*args):
    result = 0
    for i in args:
        for num in i:
            result += (num - np.mean(i))**2
    return result





print(S_2(fb, hc, wl)) # 830.9642857142858
print(S_2_F(fb, hc, wl)) # 253.9074675324678
print(S_2_REM(fb, hc, wl)) # 577.0568181818181
print(S_2_F(fb, hc, wl) + S_2_REM(fb, hc, wl)) # 830.9642857142859 расчеты верны


# Вычисляем факторую дисперсию

sig_2_F = S_2_F(fb, hc, wl) / (k-1)
print(sig_2_F) # 126.9537337662339

# Вычисляем остаточную дисперсию

sig_2_REM = S_2_REM(fb, hc, wl) / (n - k)
print(sig_2_REM) # 23.082272727272724

# Вычисляем Fн

F_n = sig_2_F / sig_2_REM
print(F_n) # 5.5


# Пользуясь таблицей критических точек распределения Фишера-Снедокера для заданного уровня статистическсой значимости и 2х степеней свободы, находим значение F_крит

F_crit = 3.34

# 5.5 > 3.34, следовательно, между группами есть статистически значимое различие.
