# -*- coding: utf-8 –*-

"""
给你一个栈，请你逆序这个栈，
不能申请额外的数据结构，
只能使用递归函数。 如何实现?
"""


def reverse(stack):
    """ 逆序栈过程
        拿栈底元素 1 ——> 递归调用 ——> 拿栈底元素 2 ——> 递归调用 ——> 拿栈底元素 3 ——> 递归调用 ——> 栈空 return
                                                                                            ↓
        将元素1压回栈 <—— 递归结束 <—— 将元素2压回栈 <—— 递归结束 <—— 将元素3压回栈 <—— 递归结束    <——
    """
    if not stack:
        return
    i = f(stack)
    reverse(stack)
    stack.append(i)


def f(stack):
    """
    栈底元素移除掉
    上面的元素盖下来
    返回移除掉的栈底元素
    """
    result = stack.pop()
    if stack:
        last = f(stack)
        stack.append(result)
        return last
    else:
        return result


if __name__ == "__main__":
    stack = [1, 2, 3]
    print stack
    reverse(stack)
    print stack