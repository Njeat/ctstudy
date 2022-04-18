# 최소,최대
import sys
sys.stdin = open("00.txt")

n = int(input())
num = list(map(int,input().split()))

print(min(num), max(num))
