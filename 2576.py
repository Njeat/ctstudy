# 홀수

import sys
sys.stdin = open("00.txt")

num = [int(input()) for _ in range(7)]
odd = []
num.sort()
result = -1
for i in range(7):
    if num[i] % 2 == 1:
        odd.append(num[i])
        result += num[i]

if result > 0:
    print(result + 1)
else:
    print(result)
print(min(odd))