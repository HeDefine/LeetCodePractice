#!/usr/bin/env python3

# https://leetcode-cn.com/problems/pascals-triangle
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    def generate(self, numRows: int) -> [[int]]:
        def getNextRow(preList: [int]) -> [int]:
            temp = list()
            for idx, v in enumerate(preList):
                if idx == 0:
                    temp.append(1)
                else:
                    temp.append(preList[idx - 1] + v)
            temp.append(1)
            return temp

        result = []
        for i in range(0, numRows):
            if i == 0:
                result.append([1])
            else:
                result.append(getNextRow(result[-1]))
        return result


print(Solution().generate(5))


# 简单题，没啥好说的
