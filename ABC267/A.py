s = input()

lst = ["Friday", "Thursday", "Wednesday", "Tuesday", "Monday"]
def check():
    for i, a in enumerate(lst, 1):
        if s == a:
            print(i)

if __name__ == "__main__":
    check()