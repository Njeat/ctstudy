# N번째 큰 수
import sys
sys.stdin = open("00.txt")

list = [list(map(int,input().split())) for _ in range(int(input()))]

for i in range(len(list)):
    list[i].sort()

for i in range(len(list)):
    print(list[i][-3])
