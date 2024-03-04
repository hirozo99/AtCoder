n = int(input())
for _ in range(n):
    l = list(input().split())
    se = []
    for i in range(n):
        if l[i] == "1":
            se.append(i+1)

    print(*se)