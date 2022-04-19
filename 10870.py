# 피보나치 수 5
import sys
sys.stdin = open("00.txt")

f = [0, 1]
fn = 0
for i in range(int(input())):
    f.append(f[i] + f[i+1])

print(f[-2])