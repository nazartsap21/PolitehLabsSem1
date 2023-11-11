from math import *

x = 6.0
a = 6
b = 9
h = 0.2

while x <= b:
    if x < 7:
        print(round(x, 2), "\t", log(x * log(x) + sin(x)))
        x += h
    elif (x >= 7) and (x < 8):
        print(round(x, 2), "\t", log(sin(x) + 4, 3))
        x += h
    elif x >= 8:
        print(round(x, 2), "\t", 1 / (16 + 1 / cos(x)))
        x += h

print("-------------#2--------------")

x = 0
m = 9
h = 0.05
d = 0.001
a = 0
b = 0.5
n = 1
sigma = 1
sum_ = 1

while x <= b:
    while fabs(sigma) >= d:
        sigma *= (pow(-1, n) * (m + n - 1) * pow(x, n)) / factorial(n)
        sum_ += sigma
        n += 1

    print(round(x, 2), "\t", sum_)
    x += h
    n = 1
    sigma = 1
    sum_ = 1

