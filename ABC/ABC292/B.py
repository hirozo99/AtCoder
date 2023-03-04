N, Q = map(int, input().split())

player = [[0] for i in range(N)]
for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        player[x-1][0] += 1
    elif c == 2:
        player[x-1][0] += 2
    else:
        if player[x-1][0] < 2:
            print("No")
        else:
            print("Yes")