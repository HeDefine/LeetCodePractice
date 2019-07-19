#!/usr/bin/env python3

# https://leetcode-cn.com/problems/add-binary
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
# 输入: a = "1010", b = "1011"
# 输出: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        v1 = int(a, 2)
        v2 = int(b, 2)
        return format((v1 + v2), "b")


print(Solution().addBinary("11", "1"))  # "100"
print(Solution().addBinary("1010", "1011"))  # "10101"
