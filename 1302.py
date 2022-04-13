# 베스트셀러

import sys
sys.stdin = open("00.txt")

n = int(input())
m = dict()
m_key = [0]*n
valueList = list()
keyList = list()

for i in range(n):
    book = input()
    m[book] = 0
    m_key[i] = book

for i in range(n):
    m[m_key[i]] += 1

reverse_m = dict(map(reversed,m.items()))

for i, j in m.items():
    keyList.append(i)
    valueList.append(j)

print(keyList,valueList)

# m.values()
# print(m)
# # print(reverse_m) # 키갑싱 같으면 오류
# print(reverse_m[max(m.values())])

