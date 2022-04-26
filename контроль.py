from math import sin, cos, radians

n = 25
B = 55.39020222
L = 144.3259289

def zone(n):
    L0 = 6*n-3
    return L0

cosB = cos(radians(B / 3600))
N = round(6399698.902 - (21562.267 - (108.973 - 0.612 * cosB ** 2) * cosB ** 2) * cosB ** 2, 8)
l0 = round((L - zone(n) * 3600) / 206265, 8)

a0 = round(32140.404 - (135.3302 - (0.7092 - 0.004 * cosB ** 2) * cosB ** 2) * cosB ** 2, 8)
a4 = round((0.25 + 0.0025 * cosB ** 2) * cosB ** 2 - 0.04166, 8)
a6 = round((0.166 * cosB ** 2 - 0.084) * cosB ** 2, 8)
a5 = round(0.0083 - (0.1667 - (0.1968 + 0.004 * cosB ** 2) * cosB ** 2) * cosB ** 2, 8)
a3 = round((0.3333333 + 0.001123 * cosB ** 2) * cosB ** 2 - 0.1666667, 8)

x = round(6367558.4969 * (B / 206265) - (a0 - (0.5 + (a4 + a6 * l0 ** 2) * l0 ** 2) * l0 ** 2 * N) * sin(
radians(B / 3600)) * cosB, 3)
y = round((1 + (a3 + a5 * l0 ** 2) * l0 ** 2) * l0 * N * cosB, 3)

print(N)
print(a0)
print(a4)
print(a6)


