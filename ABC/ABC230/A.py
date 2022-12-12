n = int(input())

k = n + 1

if n < 10:
    print("AGC00" + str(n))
elif 10 <= n <= 54:
    if 10 <= n <= 41:
        print("AGC0" + str(n))
    else:
        print("AGC0" + str(k))