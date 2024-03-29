#!/usr/bin/env python3

# https://leetcode-cn.com/problems/divide-two-integers
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 示例 1:
# 输入: dividend = 10, divisor = 3
# 输出: 3
#
# 示例 2:
# 输入: dividend = 7, divisor = -3
# 输出: -2
#
# 说明:
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        sign = 1 if dividend ^ divisor >= 0 else -1
        divd = abs(dividend)
        dior = abs(divisor)
        while divd >= dior:
            tmp, i = dior, 1
            while divd >= tmp:
                divd -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        res = res * sign
        return min(max(-2 ** 31, res), 2 ** 31 - 1)


print(Solution().divide(10, 3))  # 3
print(Solution().divide(7, -3))  # - 2
print(Solution().divide(-7, -3))  # 2
print(Solution().divide(-7, 3))  # - 2
