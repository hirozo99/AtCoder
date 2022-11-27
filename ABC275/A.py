n = int(input())
h = list(map(int, input().split()))

B = [(a, i+1) for i, a in enumerate(h)]
B.sort()
print(B[-1][1])