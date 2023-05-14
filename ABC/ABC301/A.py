N = int(input())
S = input()

t = 0
a = 0
for i in range(N):
    if S[i] == "T":
        t += 1
    else:
        a += 1

if t > a:
    print("T")
elif t < a:
    print("A")
elif t == a:
    if S[-1] == "A":
        print("T")
    else:
        print("A")