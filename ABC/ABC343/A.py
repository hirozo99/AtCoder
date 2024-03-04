A, B = map(int, input().split())
N = A + B
for i in range(10):
    if N == i:
        continue
    print(i)
    exit()