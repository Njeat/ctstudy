# 소수
import sys
sys.stdin = open("00.txt")

n, m = int(input()), int(input())
sosu = []
sum = 0
for i in range(n,m+1):
    cnt = 0
    for j in range(1,i+1):
        if i%j == 0:
            cnt += 1
    if cnt == 2:
        sosu.append(i)
        sum += i
        break

if len(sosu) < 1:
    print('-1')
else :
    print(sum)
    print(min(sosu))
