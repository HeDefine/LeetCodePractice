#!/usr/bin/env python3

# https://leetcode-cn.com/problems/excel-sheet-column-number
# 给定一个Excel表格中的列名称，返回其相应的列序号。
# 例如，
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
#
# 示例 1:
# 输入: "A"
# 输出: 1
#
# 示例 2:
# 输入: "AB"
# 输出: 28
#
# 示例 3:
# 输入: "ZY"
# 输出: 701


class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for v in s:
            if 'A' <= v <= 'Z':
                result = result * 26 + (ord(v) - ord('A') + 1)
        return result


print(Solution().titleToNumber("A"))  # 1
print(Solution().titleToNumber("AB"))  # 28
print(Solution().titleToNumber("ZY"))  # 701
print(Solution().titleToNumber("AAA"))  # 703
