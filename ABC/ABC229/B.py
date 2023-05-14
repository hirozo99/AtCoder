def judge():
    A, B = input().split()
    X, Y = A.zfill(20), B.zfill(20)
    for x, y in zip(X, Y):
        if int(x) + int(y) >= 10:
            return "Hard"
    return "Easy"

print(judge())
