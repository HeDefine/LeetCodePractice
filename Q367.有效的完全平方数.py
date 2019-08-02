#!/usr/bin/env python3

# https://leetcode-cn.com/problems/valid-perfect-square
#
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
# 说明：不要使用任何内置的库函数，如  sqrt。
#
# 示例 1：
# 输入：16
# 输出：True
#
# 示例 2：
# 输入：14
# 输出：False


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num + 1):
            if i * i == num:
                return True

            if i * i > num:
                return False

    def isPerfectSquare2(self, num: int) -> bool:
        minV = 0
        maxV = num + 1

        while minV <= maxV:
            mid = (minV + maxV) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                minV = mid + 1
            else:
                maxV = mid - 1
        return False


print(Solution().isPerfectSquare2(16))  # True
print(Solution().isPerfectSquare2(14))  # False
print(Solution().isPerfectSquare2(9))  # True
print(Solution().isPerfectSquare2(1))  # True
