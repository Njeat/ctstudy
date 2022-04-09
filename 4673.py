numlist = []
for a in range(10000):
    numlist.insert(a,a+1)

# print(numlist)
def man(m):
    return m//10000
def chun(m):
    return (man(m)%10000)//1000
def baek(m):
    return (chun(m)%1000)//100
def ship(m):
    return (baek(m)%100)//10
def ill(m):
    return (ship(m)%10)

for i in range(len(numlist)):
    n = (i+1) + man(i+1) + chun(i+1) + baek(i+1) + ship(i+1) + ill(i+1)
    if n <= 10000:
        numlist.remove(n)
    

# for i in numlist:
#     print(numlist)
print(numlist)