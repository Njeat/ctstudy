# 약수 구하기
import sys
sys.stdin = open("00.txt")

n, k = map(int,input().split())
measure = []
for i in range(1,n+1):
    if n%i == 0:
        measure.append(i)

if len(measure) < k:
    print('0')
else:
    print(measure[k-1])
