a, b, c = map(int, input().split())

if a <= b <= c:
    print("Yes")
elif a >= b >= c:
    print("Yes")
else:
    print("No")

#解説の実装例
a, b, c = map(int, input().split())
print("Yes" if a <= b <= c or a >= b >= c else "No")
