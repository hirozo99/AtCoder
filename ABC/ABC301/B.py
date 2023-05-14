N = int(input())
A = list(map(int, input().split()))

ans = []
def make_p(a, b):
    lst = []
    for i in range(a+1, b):
        lst.append(i)
    return lst

def make_m(a, b):
    lst = []
    for i in range(a-1, b, -1):
        lst.append(i)
    return lst

for i in range(N-1):
    ans.append(A[i])
    if A[i+1] - A[i] > 1:
        ans += make_p(A[i], A[i+1])
    elif A[i+1] - A[i] < 1:
        ans += make_m(A[i], A[i+1])

ans.append(A[-1])
print(*ans)
