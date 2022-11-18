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

#解説の実装例
def main():
    s = input()
    n = len(s)
    for i in range(n, 0, -1):
        if s[i - 1] == "a":
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()