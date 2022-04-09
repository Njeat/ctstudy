import sys
sys.stdin = open("00.txt")

n,m = map(int,input().split())
card = list(map(int,input().split()))
sum = 0
maxlist = []

for i in range(n-2):
    for j in range(i+1,n-1):
        for h in range(j+1,n):
            sum = card[i]+card[j]+card[h]
            if sum > m : 
                continue
            if sum <= m :
                maxlist.append(sum)

maxNum = max(maxlist)
print(maxNum)