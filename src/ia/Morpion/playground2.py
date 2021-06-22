from typing import Callable


def test():
    print(1)


def test2():
    print(2)


def test3():
    print(3)


switcher: dict[int, Callable] = {
    1: test,
    2: test2,
    3: test3
}

switcher.get(2)()
switcher.get(1)()
