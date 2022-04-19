# 지능형 기차 2
import sys
sys.stdin = open("00.txt")

result = 0
temp = 0

for i in range(10):
    out, come = map(int,input().split())
    result += come
    result -= out
    if temp < result:
        temp = result

print(temp)