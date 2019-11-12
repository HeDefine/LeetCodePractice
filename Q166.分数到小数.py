#!/usr/bin/env python3

# https://leetcode-cn.com/problems/fraction-to-recurring-decimal
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
# 如果小数部分为循环小数，则将循环的部分括在括号内。
#
# 示例 1:
# 输入: numerator = 1, denominator = 2
# 输出: "0.5"
#
# 示例 2:
# 输入: numerator = 2, denominator = 1
# 输出: "2"
#
# 示例 3:
# 输入: numerator = 2, denominator = 3
# 输出: "0.(6)"

import math


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        signal = '' if numerator * denominator >= 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)
        res1 = str(numerator // denominator)
        numerator = numerator % denominator * 10
        dic = dict()
        idx = -1
        res2 = ''
        while dic.get(numerator) is None and numerator > 0:
            idx += 1
            dic[numerator] = idx
            if numerator < denominator:
                numerator *= 10
                res2 += '0'
                continue
            res2 += str(numerator // denominator)
            numerator = numerator % denominator * 10
        if numerator != 0:
            idx = dic.get(numerator)
            res2 = res2[:idx] + '(' + res2[idx:] + ')'

        return signal + res1 + ('.' if len(res2) > 0 else '') + res2


print(Solution().fractionToDecimal(1, 2))  # 0.5
print(Solution().fractionToDecimal(2, 1))  # 2
print(Solution().fractionToDecimal(2, 3))  # 0.(6)
print(Solution().fractionToDecimal(-50, 8))  # "-6.25"
print(Solution().fractionToDecimal(2147483647, 37))  # "58040098.(567)"
