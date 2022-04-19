# 일곱난쟁이
import sys
sys.stdin = open("00.txt")

height = [int(input()) for _ in range(9)]
sum = sum(height)

for i in range(9):
    for j in range(i+1, 9):
        if 100 == sum - (height[i] + height[j]):
            num1, num2 = height[i], height[j]
            height.remove(num1)
            height.remove(num2)
            height.sort()
            
            for i in height:
                print(i)
            break

    if len(height) < 9:
        break