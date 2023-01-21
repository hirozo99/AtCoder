import itertools
N, X = map(int, input().split())

A_list = []
B_list = []

for i in range(N):
    A, B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)

for i in range(N):
    for j in range(B_list[i]+1):
        for k in range(j):
            print(j, k)

print(A_list)
print(B_list)

