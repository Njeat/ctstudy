import sys

sys.stdin = open("00.txt")

n, m = map(int, input().split())
card = list(map(int,input().split()))
# def go(index, sum, r):
#     if sum > m : return
#     if r == 0: return

#     sum += card[index]
    
#     go(index+1, sum, r)     # 사용 안할 때
#     go(index+1, sum, r-1)   # 사용 할 때

# n, m = map(int, input().split())
# card = list(map(int,input().split()))
# sum = 0
# go(0,0,3)