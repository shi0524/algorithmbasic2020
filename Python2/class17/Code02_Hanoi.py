# -*- coding: utf-8 –*-

def hanoi1(n):
    left_to_right(n)


def left_to_right(n):
    """ 把1~N层圆盘 从左 -> 右
    """
    if n == 1:
        print('Move 1 from left to right')
        return
    else:
        left_to_mid(n - 1)
        print("Move {} from left to right".format(n))
        mid_to_right(n - 1)


def left_to_mid(n):
    """ 把1~N层圆盘 从左 -> 中
    """
    if n == 1:
        print("Move 1 from left to mid")
    else:
        left_to_right(n - 1)
        print("Move {} from left to mid".format(n))
        right_to_mid(n - 1)


def mid_to_right(n):
    """ 把1~N层圆盘 从中 -> 右
    """
    if n == 1:
        print("Move 1 from mid to right")
    else:
        mid_to_left(n - 1)
        print("Move {} from mid to right".format(n))
        left_to_right(n - 1)


def mid_to_left(n):
    """ 把1~N层圆盘 从中 -> 左
    """
    if n == 1:
        print("Move 1 from mid to left")
    else:
        mid_to_right(n - 1)
        print("Move {} from mid to left".format(n))
        right_to_left(n - 1)


def right_to_left(n):
    """ 把1~N层圆盘 从右 -> 左
    """
    if n == 1:
        print("Move 1 from right to left")
    else:
        right_to_mid(n - 1)
        print("Move {} from right to left".format(n))
        mid_to_left(n - 1)


def right_to_mid(n):
    """ 把1~N层圆盘 从右 -> 中
    """
    if n == 1:
        print("Move 1 from right to mid")
    else:
        right_to_left(n - 1)
        print("Move {} from right to mid".format(n))
        left_to_mid(n - 1)


def hanoi2(n):
    if (n > 0):
        func(n, "left", "right", "mid")


def func(n, _from, _to, another):
    if n == 1:
        print("Move 1 from {} to {}".format(_from, _to))
    else:
        func(n - 1, _from, another, _to)
        print("Move {} from {} to {}".format(n, _from, _to))
        func(n - 1, another, _to, _from)


def hanoi3(n):
    """ 汉诺塔迭代版
    """
    stack = []
    stack.append({"finish": False, "base": n, "from": "left", "to": "right", "another": "mid"})
    while stack:
        task = stack.pop()
        if task["base"] == 1:
            print("Move 1 from {} to {}".format(task["from"], task["to"]))
            if stack:
                stack[-1]["finish"] = True
        else:
            if not task["finish"]:
                stack.append(task)
                stack.append({"finish": False, "base": task["base"] -1, "from": task["from"], "to": task["another"], "another": task["to"]})
            else:
                print("Move {} from {} to {}".format(task["base"], task["from"], task["to"]))
                stack.append({"finish": False, "base": task["base"] -1, "from": task["another"], "to": task["to"], "another": task["from"]})


if __name__ == "__main__":
    n = 3
    hanoi1(n)
    print("*" * 25)
    hanoi2(n)
    print("*" * 25)
    hanoi3(n)


