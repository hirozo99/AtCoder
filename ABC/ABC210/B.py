def main():
    N = int(input())
    S = input()
    x = S.index('1')  # はじめに'1'が出現するインデックス
    print('Takahashi' if x % 2 == 0 else 'Aoki')  # 負ける人を答えるのに注意


if __name__ == '__main__':
    main()