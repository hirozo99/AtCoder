import sys
input = sys.stdin.readline
S = input()
T = input()

for i in range(len(S)):
    if S[i] != T[i]:
        print(i+1)
        break

