#解説の実装例
def main():
    s = input()
    n = len(s)
    for i in range(n, 0, -1):
        if s[i - 1] == "a":
            print(i)
            return
    print(-1)

if __name__ == "__main__":
    main()