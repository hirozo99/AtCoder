def main():
    def solve():
        if len(set(X)) == 1:
            return 'Weak' # Xの文字種が1種類のみです
        for i in range(3):
            if (int(X[i]) + 1) % 10 != int(X[i + 1]):
                return 'Strong' # 1箇所でも連続していなければ、その時点で強いパスワードです
        return 'Weak'  # 1234のような4連続の数字なので、弱いパスワードです

    X = input()
    print(solve())


if __name__ == '__main__':
    main()