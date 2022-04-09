# import sys

# sys.stdin = open("00.txt")

w = [0]*10
k = [0]*10
for i in range(len(w)):
    n = int(input())
    w[i] = n
# for i in range(len(k)):
#     n = int(input())
#     k[i] = n

w.sort()
w.reverse()
print(w)

