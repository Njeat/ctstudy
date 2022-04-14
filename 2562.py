# 최댓값
import sys
sys.stdin = open("00.txt")

num = []
for _ in range(9):
    num.append(int(input()))
    
for i in range(len(num)):
    if num[i] == max(num):
        print(max(num), i+1, sep="\n")