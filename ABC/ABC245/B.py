N = int(input())
A = list(map(int, input().split()))

A = set(A)
array = []
for i in range(2001):
    if i in A:
        array.append(i)
    else:
        print(i)
        exit()
