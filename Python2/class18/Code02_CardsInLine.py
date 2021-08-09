# -*- coding: utf-8 –*-

def win1(arr):
    fst = first(0, len(arr) - 1, arr)
    scd = second(0, len(arr) - 1, arr)
    return fst if fst >= scd else scd


def first(l, r, arr):
    """ 先手
    """
    if l == r:
        return arr[l]
    choice_l = arr[l] + second(l + 1, r, arr)
    choice_r = arr[r] + second(l, r - 1, arr)
    return max(choice_l, choice_r)


def second(l, r, arr):
    """ 后手
    """
    if l == r:
        return 0
    choice_l = first(l + 1, r, arr)
    choice_r = first(l, r - 1, arr)
    return min(choice_l, choice_r)


def win2(arr):
    n = len(arr)
    fst_dp = [[-1] * n for _ in range(n)]
    scd_dp = [[-1] * n for _ in range(n)]
    fst = first2(0, len(arr) - 1, arr, fst_dp, scd_dp)
    scd = second2(0, len(arr) - 1, arr, fst_dp, scd_dp)
    return fst if fst >= scd else scd


def first2(l, r, arr, fst_dp, scd_dp):
    """ 先手
    """
    if fst_dp[l][r] != -1:
        return fst_dp[l][r]
    if l == r:
        ans = arr[l]
    else:
        choice_l = arr[l] + second2(l + 1, r, arr, fst_dp, scd_dp)
        choice_r = arr[r] + second2(l, r - 1, arr, fst_dp, scd_dp)
        ans = max(choice_l, choice_r)
    fst_dp[l][r] = ans
    return ans


def second2(l, r, arr, fst_dp, scd_dp):
    """ 后手
    """
    if scd_dp[l][r] != -1:
        return scd_dp[l][r]
    if l == r:
        ans = 0
    else:
        choice_l = first2(l + 1, r, arr, fst_dp, scd_dp)
        choice_r = first2(l, r - 1, arr, fst_dp, scd_dp)
        ans = min(choice_l, choice_r)
    scd_dp[l][r] = ans
    return ans


def win3(arr):
    n = len(arr)
    fst_dp = [[0] * n for _ in range(n)]
    scd_dp = [[0] * n for _ in range(n)]

    # base case (先手为对应位置, 后手为0)
    for l in range(n):
        fst_dp[l][l] = arr[l]
    # 普遍位置
    for start_col in range(1, n):
        l = 0
        r = start_col
        while r < n:
            fst_dp[l][r] = max(arr[l] + scd_dp[l + 1][r], arr[r] + scd_dp[l][r - 1])
            scd_dp[l][r] = min(fst_dp[l + 1][r], fst_dp[l][r - 1])
            l += 1
            r += 1
    return fst_dp[0][n-1] if fst_dp[0][n-1] >= scd_dp[0][n-1] else scd_dp[0][n-1]


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    ans1 = win1(arr)
    ans2 = win2(arr)
    ans3 = win3(arr)
    print(ans1, ans2, ans3)