#!/usr/bin/env python3

# https://leetcode-cn.com/problems/multiply-strings
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
#
# 示例 2:
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
# 说明：
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def plus(n1: str, n2: str) -> str:
            sumV = ''
            if len(n2) > len(n1):
                n1, n2 = n2, n1
            for idx in range(-1, -len(n1) - 1, -1):
                val1 = int(n1[idx])
                val2 = int(n2[idx]) if idx > -len(n2) - 1 else 0
                if idx > -len(sumV) - 1:
                    sumV = str(int(sumV[idx]) + val1 + val2) + sumV[idx + 1:]
                else:
                    sumV = str(val1 + val2) + sumV
            return sumV

        def multi(n1: str, num: str) -> str:
            multiV = ''
            for idx in range(-1, -len(n1) - 1, -1):
                val1 = int(n1[idx])
                val2 = int(num)

                if idx > -len(multiV) - 1:
                    multiV = str(val1 * val2 + int(multiV[idx])) + multiV[idx + 1:]
                else:
                    multiV = str(val1 * val2) + multiV
            return multiV

        if len(num2) > len(num1):
            num1, num2 = num2, num1
        if num2 == '0' or num1 == '0':
            return '0'
        res = ''
        for idx in range(-1, -len(num2) - 1, -1):
            temp = multi(num1, num2[idx])
            if idx == -1:
                res = plus(temp, res)
            else:
                res = plus(temp + '0' * (abs(idx) - 1), res)

        return res


print(Solution().multiply('2', '3'))  # 6
print(Solution().multiply('123', '456'))  # "56088"
