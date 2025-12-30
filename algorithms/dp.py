import sys


def how_sum(target, arr):
    dp = [None] * (target + 1)
    dp[0] = []

    for i in range(target + 1):
        if dp[i] is not None:
            for j in arr:
                if i + j <= target:
                    dp[i + j] = dp[i] + [j]

    return dp[target]


def best_sum(target, arr):
    dp = [None] * (target + 1)
    dp[0] = []

    for i in range(target + 1):
        if dp[i] is not None:
            for j in arr:
                if i + j <= target:
                    new_comb = dp[i] + [j]
                    if dp[i + j] is None or len(dp[i + j]) > len(new_comb):
                        dp[i + j] = new_comb

    return dp[target]


def min_steps(k):
    dp = [sys.maxsize] * (k + 1)
    dp[0] = 0

    for i in range(k + 1):
        if i + 1 <= k:
            dp[i + 1] = min(dp[i] + 1, dp[i + 1])
        if i * 2 <= k:
            dp[i * 2] = min(dp[i] + 1, dp[i * 2])

    return dp[k]


def max_rod_segments(n, x, y, z):
    """Given a rod of length n,
    the task is to cut the rod in such a way that the
    total number of segments of length x, y, and z is maximized."""
    dp = [None] * (n + 1)
    dp[0] = []

    for i in range(n + 1):
        if dp[i] is not None:
            for j in (x, y, z):
                if i + j <= n:
                    new_comb = dp[i] + [j]
                    if dp[i + j] is None or len(dp[i + j]) < len(new_comb):
                        dp[i + j] = new_comb

    return 0 if dp[n] is None else len(dp[n])


# EXTREMELY IMPORTANT
def catalan(n):
    """catalan(n'th term) = 2n! / [(n+1)! * n!]"""
    if n == 0:
        return 1
    dp = [i for i in range(2 * n + 1)]
    dp[0] = 1

    for i in range(1, 2 * n + 1):
        dp[i] *= dp[i - 1]

    return dp[2 * n] // (dp[n + 1] * dp[n])


def valid_parenthesis(n):
    """n = 4 -> 2 i.e. catalan(n/2) ["(())" and "()()" ] (n has to be even)"""
    return 0 if n % 2 != 0 else catalan(n // 2)


def polygon_triangulation(n):
    """Given a convex polygon with n sides. The task
    is to calculate the number of ways in which triangles can be
    formed by connecting vertices with non-crossing line segments."""
    return 0 if n < 2 else catalan(n - 2)


def unique_bst(n):
    """Given an integer n, the task is to find the total
    number of unique BSTs that can be made using values from 1 to n."""
    return catalan(n)


def binary_trees(n):
    """Number of full binary trees with n internal nodes"""
    return catalan(n)


def minimum_sum_path_triangle(arr, i=0, j=0, dp={}):
    """Given a triangular array, find the minimum path sum from top to bottom.
        For each step, we can move to the adjacent numbers of the row
        below. i.e., if we are on an index i of the current row,
        we can move to either index i or index i + 1 on the next row.

        Input: triangle[][] =  [[2],
                                [3, 7],
                                [8, 5, 6],
                                [6, 1, 9, 3]]
    Output: 11
    Explanation : The path is 2 → 3 → 5 → 1, which results in a minimum sum of 2 + 3 + 5 + 1 = 11"""

    if (i, j) in dp:
        return dp[(i, j)]
    if i == len(arr) - 1:
        return arr[i][j]

    lv1 = minimum_sum_path_triangle(arr, i + 1, j, dp)
    lv2 = minimum_sum_path_triangle(arr, i + 1, j + 1, dp)
    dp[(i, j)] = arr[i][j] + min(lv1, lv2)

    return dp[(i, j)]


def min_cost_path(arr, i=0, j=0, dp={}):
    if (i, j) in dp:
        return dp[(i, j)]

    m = len(arr)
    n = len(arr[0])
    if i == m or j == n:
        return sys.maxsize
    if i == m - 1 and j == n - 1:
        return arr[i][j]

    dp[(i, j)] = arr[i][j] + min(
        min_cost_path(arr, i, j + 1),
        min_cost_path(arr, i + 1, j + 1),
        min_cost_path(arr, i + 1, j),
    )

    return dp[(i, j)]


def jump_game(arr):
    n = len(arr)
    dp = [sys.maxsize] * n
    dp[0] = 0

    for i in range(n):
        for j in range(1, arr[i] + 1):
            if i + j < n:
                dp[i + j] = min(dp[i + j], dp[i] + 1)

    return -1 if dp[-1] == sys.maxsize else dp[-1]


def longest_common_substring(str1, str2):
    l1, l2, res, end = len(str1), len(str2), 0, 0
    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if dp[i][j] > res:
                    res = dp[i][j]
                    end = i

    return res, str1[end - res : end]


def longest_common_subsequence(str1, str2):
    l1, l2 = len(str1), len(str2)
    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[l1][l2]

