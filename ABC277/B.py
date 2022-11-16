# N = int(input())
# S = [input() for _ in range(N)]
#
# def is_ans():
#     for i in range(N):
#         if S[i].find("H" or "D" or "C" or "S") == 0:
#             if S[i].find("A" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "T" or "J" or "Q" or "K" ) == 1:
#                 return True
#         return False
#
# if is_ans():
#     print("Yes")
# elif not is_ans():
#     print("No")

n = int(input())
s = [input() for _ in range(n)]
s1 = "HDCS"
s2 = "A23456789TJQK"
ans = True
for i in range(n):
	for j in range(i):
		print(i, j)
		if s[i] == s[j]:
			ans = False
for i in range(n):
	if not s1.count(s[i][0]) or not s2.count(s[i][1]):
		ans = False
print("Yes" if ans else "No")
