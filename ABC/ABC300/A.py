N, A, B = map(int, input().split())
c = list(map(int, input().split()))

num = A + B
for i in range(N):
    if c[i] == num:
        print(i+1)
        exit()