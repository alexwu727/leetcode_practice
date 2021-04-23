def f1():
    print("hello")


def f2():
    print("world")


def f3(n: int = 0):
    print(n)


def f4(n: int):
    print(n * n)


if __name__ == '__main__':
    arr = []
    arr.append(f1)
    arr.append(f2)
    arr.append(f3)
    for f in arr:
        f()
