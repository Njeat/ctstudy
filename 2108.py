# 통계학
import sys
sys.stdin = open("00.txt")

n = int(input())
m = []
howmany = dict()

for _ in range(n):
    i = int(input())
    m.append(i)
    howmany[i] = 0

u = sorted(m)

for i in u:
    howmany[i] += 1

tmp = howmany[u[0]]

for i in range(len(howmany)-1):
    # print(howmany[u[i]])
    # print(howmany[u[i]])
    if howmany[u[i]] <= howmany[u[i+1]]:
        tmp = u[i+1]

print(round(sum(m)/n))
print(u[(n//2)])
print(tmp)
print(u[-1]-u[0])