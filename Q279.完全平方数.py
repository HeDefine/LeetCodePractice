#!/usr/bin/env python3

# https://leetcode-cn.com/problems/perfect-squares
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 示例 1:
# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
#
# 示例 2:
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.

from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1, 1):
            for j in range(1, n + 1, 1):
                if j ** 2 > i:
                    break
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[-1]


# print(Solution().numSquares(12))
# print(Solution().numSquares(13))
# print(Solution().numSquares(6922))
print(Solution().numSquares(5812))
