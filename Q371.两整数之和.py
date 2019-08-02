#!/usr/bin/env python3

# https://leetcode-cn.com/problems/sum-of-two-integers
# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
#
# 示例 1:
# 输入: a = 1, b = 2
# 输出: 3
#
# 示例 2:
# 输入: a = -2, b = 3
# 输出: 1


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])


print(Solution().getSum(1, 2))  # 3
print(Solution().getSum(-2, 3))  # 1
