# 소수 찾기
import sys
sys.stdin = open("00.txt")

n = int(input())
list = list(map(int,input().split()))
result = []
for i in list:
    cnt = 0
    for j in range(1,i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        result.append(i)

print(len(result))