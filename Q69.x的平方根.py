#!/usr/bin/env python3

# https://leetcode-cn.com/problems/sqrtx
# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
# 输入: 4
# 输出: 2
#
# 示例 2:
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。

class Solution:
    def mySqrt(self, x: int) -> int:
        minV = 0
        maxV = x
        if x == 1:
            return 1
        while minV <= maxV:
            midV = (minV + maxV) // 2
            p1 = midV * midV
            p2 = (midV + 1) * (midV + 1)
            if p1 <= x < p2:
                return midV
            elif x >= p2:
                minV = midV
            else:
                maxV = midV


# print(Solution().mySqrt(4))  # 2
# print(Solution().mySqrt(8))  # 2
# print(Solution().mySqrt(16))  # 2

# print(Solution().mySqrt(2))  # 2
print(Solution().mySqrt(1))
# print(Solution().mySqrt(0))  # 2


# 解题思路： 二分法查找
