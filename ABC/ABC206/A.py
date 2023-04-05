N = int(input())

check = 1.08 * N // 1
if check < 206:
    print("Yay!")
elif check == 206:
    print("so-so")
else:
    print(":(")