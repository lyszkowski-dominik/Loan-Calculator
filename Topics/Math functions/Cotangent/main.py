from math import sin
from math import cos
from math import radians

degrees = int(input())
rads = radians(degrees)
cotangent = cos(rads) / sin(rads)
print(round(cotangent, 10))