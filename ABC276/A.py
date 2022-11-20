s = str(input())
s_list = list(s)
ans = []
for i in range(len(s_list)):
    if s_list[i] == "a":
        ans.append(i+1)
def main():
    if ans:
        print(ans[-1])
    else:
        print(-1)

if __name__=='__main__':
    main()

