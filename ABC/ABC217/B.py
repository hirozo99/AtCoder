a = ['ABC', 'ARC', 'AGC', 'AHC']
b = []
for i in range(3):
    S = input()
    b.append(S)

for i in range(4):
    if a[i] in b:
        pass
    else:
        print(a[i])
        exit()