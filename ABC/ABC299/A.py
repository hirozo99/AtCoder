N = int(input())
S = input()

a = S.find("|")
b = S.find("*")
c = S.rfind("|")

if a < b < c:
    print("in")
else:
    print("out")