# 별찍기 - 1

from re import I
import sys
sys.stdin = open("00.txt")

n = int(input())

for i in range(1,n+1):
    print(' '* (n-i) + '*' *i + '*' * (i-1))
for i in range(1,n+1):
    print(' ' * i + '*' * (n-i) + '*' * (n-i-1))