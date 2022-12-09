a, b, c, x = map(int, input().split())

if a >= x:
    print(f'{1:.12f}')
elif a + 1 <= x <= b:
    print(f'{c / (b - a):.12f}')
elif b <= x:
    print(f'{0:.12f}')