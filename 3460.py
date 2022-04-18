# 이진수
import sys
sys.stdin = open("00.txt")

for _ in range(int(input())):
    n = int(input())
    b = bin(n)[2:]
    # print(len(b))
    for i in range(len(b)):
        if b[::-1][i] == '1':
            print(i, end=' ')
    print()