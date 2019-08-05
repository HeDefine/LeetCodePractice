#!/usr/bin/env python3

# https://leetcode-cn.com/problems/add-strings
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
# 注意：
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        resultStr = ""
        for idx in range(1, max(len(num1), len(num2)) + 1):
            temp = 0
            if idx <= len(num1):
                temp += ord(num1[-idx]) - ord("0")

            if idx <= len(num2):
                temp += ord(num2[-idx]) - ord("0")

            if idx <= len(resultStr):
                temp += ord(resultStr[0]) - ord("0")
                resultStr = str(temp) + resultStr[1:]
            else:
                resultStr = str(temp) + resultStr
        return resultStr


print(Solution().addStrings("1", "1"))
