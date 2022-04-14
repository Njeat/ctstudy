# 카이사르 암호

import sys
sys.stdin = open("00.txt")
after = list(input())

for i in range(len(after)):
    k = ord(after[i])-3
    if k < ord('A'):
        k += 26
    after[i] = chr(k)

print("".join(after))
# answer = list

