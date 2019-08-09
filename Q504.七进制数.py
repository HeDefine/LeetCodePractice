#!/usr/bin/env python3

# https://leetcode-cn.com/problems/base-7
# 给定一个整数，将其转化为7进制，并以字符串形式输出。
#
# 示例 1:
# 输入: 100
# 输出: "202"
#
# 示例 2:
# 输入: -7
# 输出: "-10"
# 注意: 输入范围是 [-1e7, 1e7] 。


class Solution:
    def convertToBase7(self, num: int) -> str:
        signal = "" if num >= 0 else "-"
        result = ""
        num = abs(num)
        while num > 0:
            result = str(num % 7) + result
            num = num // 7
        return (signal + result if len(result) > 0 else "0")


print(Solution().convertToBase7(101))  # "202"
print(Solution().convertToBase7(-7))  # "-10"
print(Solution().convertToBase7(0))  # "-10"
