# 팩토리얼
import sys
sys.stdin = open("00.txt")

num = int(input())
result = 1
for i in range(1,num+1):
    result *= i

print(result)

