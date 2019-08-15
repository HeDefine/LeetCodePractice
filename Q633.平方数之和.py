#!/usr/bin/env python3

# https://leetcode-cn.com/problems/sum-of-square-numbers
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c。
#
# 示例1:
# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
#
# 示例2:
# 输入: 3
# 输出: False

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        for i in range(round(math.sqrt(c)), -1, -1):
            if c - i ** 2 > 0:
                v = round(math.sqrt(c - i * i))
                if v ** 2 + i ** 2 == c:
                    return True
        return False


print(Solution().judgeSquareSum(5))
print(Solution().judgeSquareSum(4))
print(Solution().judgeSquareSum(3))
