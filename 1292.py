# 쉽게 푸는 문제
import sys
sys.stdin = open("00.txt")

a, b = map(int,input().split())
list = []
sum = 0
for i in range(1,1000+1):
    for j in range(i):
        list.append(i)

for i in range(a-1,b):
    sum += list[i]
print(sum)