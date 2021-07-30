# -*- coding: utf-8 –*-

"""
请把一段纸条竖着放在桌子上，然后从纸条的下边向上方对折1次，压出折痕后展开。
此时折痕是凹下去的，即折痕突起的方向指向纸条的背面。
如果从纸条的下边向上方连续对折2次，压出折痕后展开，此时有三条折痕，从上到下依次是下折痕、下折痕和上折痕。
给定一个输入参数N，代表纸条都从下边向上方连续对折N次。 请从上到下打印所有折痕的方向。
例如:N=1时，打印: down N=2时，打印: down down up
"""

"""
一棵特殊的二叉树
树的 头结点为 凹
树的 左子树头结点为凹
树的 右子树头结点为凸

                                凹


               凹                                凸

     凹                 凸                凹                凸

凹        凸       凹        凸       凹        凸       凹       凸
"""


def print_all_folds(N):
    in_order(1, N, True)
    print("")


def in_order(i, N, down):
    """
    当前你来了一个节点，脑海中想象的！
    这个节点在第i层，一共有N层，N固定不变的
    这个节点如果是凹的话，down = T
    这个节点如果是凸的话，down = F
    函数的功能：中序打印以你想象的节点为头的整棵树！
    :param i: 当前第 i 层
    :param N: 总共N层
    :param down: 是否是凹折痕
    :return:
    """
    if i > N:
        return
    in_order(i + 1, N, True)
    print("凹" if down else "凸"),
    in_order(i + 1, N, False)


if __name__ == "__main__":
    for i in range(1, 6):
        print_all_folds(i)
