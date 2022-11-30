import sys
input = sys.stdin.readline
s = input()

if s[0] != s[1] and s[0] != s[2]:
    print(s[0])
elif s[0] != s[1] and s[0] == s[2]:
    print(s[1])
elif s[0] == s[1] and s[0] != s[2]:
    print(s[2])
else:
    print(-1)