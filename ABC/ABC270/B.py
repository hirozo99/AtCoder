x, y, z = map(int, input().split())

if 0<y<x<z or 0<y<z<x or x<z<y<0 or z<x<y<0:
    print(-1)
elif x<y<0<z or z<0<y<x:
    print(abs(z)*2+abs(x))
else:
    print(abs(x))

