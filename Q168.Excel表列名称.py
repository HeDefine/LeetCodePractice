#!/usr/bin/env python3

# https://leetcode-cn.com/problems/excel-sheet-column-title
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 例如，
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
#
# 示例 1:
# 输入: 1
# 输出: "A"
#
# 示例 2:
# 输入: 28
# 输出: "AB"
#
# 示例 3:
# 输入: 701
# 输出: "ZY"


class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n > 0:
            if n % 26 == 0:
                ch = "Z"
                n -= 26
            else:
                ch = chr(n % 26 + ord('A') - 1)
            result = ch + result
            n = n // 26
        return result


print(Solution().convertToTitle(1))  # "A"
print(Solution().convertToTitle(28))  # "AB"
print(Solution().convertToTitle(701))  # "ZY"
print(Solution().convertToTitle(52))  # AZ

# 题解: 没啥好说的。 值得注意的是 0 对应的值 'Z'
