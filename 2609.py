# 최대공약수와 최소공배수
import sys
sys.stdin = open("00.txt")

n, m = map(int,input().split())
print(n,m)
max = []
i = 0
# while True:
#     if n // i == m // i:
#         max.append(i)
    
    
while True:
    i += 1
    if n * i == m * i:
        print(n*i)
        break