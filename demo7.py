#!/usr/bin/env python3
# coding=utf-8

# https://leetcode-cn.com/problems/reverse-integer

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#
#  示例 2:
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
# 请根据这个假设，如果反转后整数溢出那么就返回 0。


class Solution:
    def reverse(self, x: int) -> int:
        isOverZero = x >= 0
        s = str(abs(x))
        temp = list(s)
        temp.reverse()
        reverseStr = "".join(temp)
        resultInt = int(reverseStr);
        if not isOverZero:
            resultInt = -1 * resultInt

        if resultInt < -pow(2, 31) or resultInt > pow(2, 31) - 1:
            resultInt = 0
        return resultInt


print(Solution().reverse(1534236469))
