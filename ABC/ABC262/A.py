import sys
input = sys.stdin.readline
y = int(input())

check = y % 4
if check == 2:
    print(y)
elif check == 1:
    print(y+1)
elif check == 0:
    print(y+2)
elif check == 3:
    print(y+3)
