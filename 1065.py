#한수

n = int(input())
s = str(n)
cnt = 0

if len(s) <= 2 :
    cnt += n
else :
    cnt += 99
    for i in range(100,n+1):
        snum = str(i)
        if(int(snum[0])-int(snum[1]) == int(snum[1])-int(snum[2])):
            cnt += 1

print(cnt)