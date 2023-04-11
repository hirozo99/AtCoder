A, B = map(int, input().split())

count = 0
while A != B:
    if A > B:
        A -= B
    else:
        B -= A
    count += 1

print(count)
