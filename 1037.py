# 약수
import sys
sys.stdin = open("00.txt")

num = int(input())
measure = list(map(int,input().split()))
print(max(measure)*min(measure))