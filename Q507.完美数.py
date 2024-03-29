#!/usr/bin/env python3

# https://leetcode-cn.com/problems/perfect-number
# 对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
# 给定一个 整数 n， 如果他是完美数，返回 True，否则返回 False
#
# 示例：
# 输入: 28
# 输出: True
# 解释: 28 = 1 + 2 + 4 + 7 + 14
#  
# 提示：
# 输入的数字 n 不会超过 100,000,000. (1e8)


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 0:
            return False
        sumV = 0
        i = 1
        while i ** 2 < num:
            if num % i == 0:
                sumV += i
                sumV += num // i
            i += 1
        return sumV == 2 * num


print(Solution().checkPerfectNumber(28))
