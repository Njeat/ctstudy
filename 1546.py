# 평균
import sys
sys.stdin = open("00.txt")

n = int(input())
num = list(map(int,input().split()))
sum = 0

for i in range(n):
    sum += num[i]

print(sum/max(num)*100/n)
