# 알파벳 찾기
import sys
sys.stdin = open("00.txt")

word = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    if i in word:
        print(word.index(i), end=' ')
    else:
        print('-1', end=' ')


# 97~122
