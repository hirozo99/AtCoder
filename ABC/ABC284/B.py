T = int(input())

s = []
def is_odd():
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] % 2 != 0:
            ans += 1
    s.append(ans)

for t in range(T):
    is_odd()

for i in range(T):
    print(s[i])