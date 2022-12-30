import sys
import math

A, B, V = map(int,sys.stdin.readline().split())
day = 0
day = (V-B)/(A-B)

print(math.ceil(day))