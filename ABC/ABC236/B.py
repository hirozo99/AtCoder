n = int(input())
count = [0] * (n + 1)
for a in map(int, input().split()):
    count[a] += 1
for i in range(1, n + 1):
    if count[i] == 3:
        print(i)
