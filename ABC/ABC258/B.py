n=int(input())
a=[list(input()) for _ in range(n)]
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]
ans = 0
for sx in range(n):
    for sy in range(n):
        for k in range(8):
            x = sx
            y = sy
            tmp = 0
            for i in range(n):
                tmp = tmp * 10 + int(a[x][y])
                x += dx[k]
                y += dy[k]
                x = (x+n)%n
                y = (y+n)%n
            ans = max(ans,tmp)
print(ans)
