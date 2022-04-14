# 별찍기 - 1

import sys
sys.stdin = open("00.txt")

n = int(input())

for i in range(n):
    print('*' * (n-i))