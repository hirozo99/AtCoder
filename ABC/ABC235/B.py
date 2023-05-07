N = int(input())
H = list(map(int, input().split()))

count = 0
while count+1 < N and H[count] < H[count+1]:
    count += 1
print(H[count])
