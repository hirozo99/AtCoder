import sys
input = sys.stdin.readline
n = list(map(int, input().split()))

n.sort()
if (n[0] == n[1] and n[2] == n[4]) or (n[0] == n[2] and n[3] == n[4]):
    print("Yes")
else:
    print("No")

