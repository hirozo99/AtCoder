import math
T = int(input())
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


k = [1, 1]
n =[]
for t in range(T):
    N = int(input())
    n.append(N)

for t in range(T):
    if n[t] == 1:
        print(*k)
    else:
        print(factorization(n[t])[0][0], factorization(n[t])[1][0])


