# 덩치

import sys
sys.stdin = open("00.txt")

n = int(input())
height = [0]*n
might = [0]*n
for i in range(n):
    a, b = map(int, input().split())
    height[i] = a
    might[i] = b

for i in range(n):
    count = 1
    for j in range(n):
        if height[i] < height[j] and might[i] < might[j]:
            count += 1
        # elif height[i] < height[j] and might[i] < might[j]:
        #     count[j] += 1
    
    print(count, end=" ")


# for i in range(len(count)):
#     print(count[i], end=" ")