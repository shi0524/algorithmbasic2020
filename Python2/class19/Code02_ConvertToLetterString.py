# -*- coding: utf-8 –*-

"""
规定1和A对应、2和B对应、3和C对应...26和Z对应
那么一个数字字符串比如"111”就可以转化为:
"AAA"、"KA"和"AK"
给定一个只有数字字符组成的字符串str，返回有多少种转化结果
"""
import random


def number(s):
    if not s:
        return 0
    return process(s, 0)


def process(s, i):
    """
    s[0..i-1]转化无需过问
    s[i.....]去转化，返回有多少种转化方法
    """
    if i == len(s):
        return 1
    # 字符重 '1' 开始的, '0'不能单独转化 只能借助前1位 转化为 10 或 20
    if s[i] == '0':
        return 0
    # s[i] != '0'
    # 可能性1, i 单传
    ways = process(s, i + 1)
    # 可能性2, 如果后边还有字符, 可和后面联合  10 ~ 26
    if i + 1 < len(s) and int(s[i:i + 2]) < 27:
        ways += process(s, i + 2)
    return ways


def ways_dp1(s):
    """
    从右往左的动态规划
    就是上面方法的动态规划版本
    dp[i]表示：str[i...]有多少种转化方式
    """
    if not s:
        return 0
    N = len(s)
    dp = [0] * (N + 1)
    dp[N] = 1
    for i in range(N - 1, -1, -1):
        if s[i] != '0':
            dp[i] = dp[i + 1]
            if i + 1 < N and int(s[i:i+2]) < 27:
                dp[i] += dp[i + 2]
    return dp[0]


def ways_dp2(s):
    """
    从左往右的动态规划
    dp[i]表示：str[0...i]有多少种转化方式
    """
    if not s or s[0] == '0':
        return 0
    N = len(s)
    dp = [0] * N
    dp[0] = 1
    for i in range(1, N):
        if s[i] == '0':
            # 如果此时str[i] == '0', 那么它肯定是要拉前一个字符一起拼
            # 那么就要求前一个字符，不能也是‘0’，否则拼不了。
            # 前一个字符不是‘0’就够了嘛？不够，还得要求拼完了要么是10，要么是20，如果更大的话，拼不了。
            # 这就够了嘛？还不够，你们拼完了，还得要求str[0...i-2]真的可以被分解！
            # 如果str[0...i-2]都不存在分解方案，那i和i-1拼成了也不行，因为之前的搞定不了。
            if s[i - 1] == '0' or s[i-1] > '2' or (i - 2 >= 0 and dp[i - 2] == 0):
                return 0
            else:
                dp[i] = dp[i - 2] if i - 2 >= 0 else 1
        else:
            dp[i] = dp[i - 1]
            if s[i - 1] != '0' and int(s[i-1: i+1]) < 27:
                dp[i] += dp[i - 2] if i - 2 >= 0 else 1
    return dp[N - 1]


def randomString(maxSize):
    _len = random.randint(1, maxSize)
    str_list = [str(random.randint(1, 26)) for _ in range(_len)]
    return "".join(str_list)[:_len]


if __name__ == "__main__":
    testTime = 10000
    maxSize = 20
    print("测试开始")
    for i in xrange(testTime):
        s = randomString(maxSize)
        ans1 = number(s)
        ans2 = ways_dp1(s)
        ans3 = ways_dp2(s)
        if ans1 != ans2 or ans1 != ans3:
            print(s)
            print(ans1)
            print(ans2)
            print(ans3)
            print("test break because of error !!!")
            break
    print("测试结束")
