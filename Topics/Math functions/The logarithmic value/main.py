from math import log

x = int(input())
base = int(input())

if base > 1:
    print(round(log(x, base), 2))
else:
    print(round(log(x), 2))