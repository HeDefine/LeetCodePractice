#!/usr/bin/env python3

# https://leetcode-cn.com/problems/maximal-square
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
# 示例:
# 输入:
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4


class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        res = 0
        sumMatrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for x, line in enumerate(matrix):
            for y, val in enumerate(line):
                if val == '1':
                    if x > 0 and y > 0 and matrix[x - 1][y - 1] == '1':
                        n = sumMatrix[x - 1][y - 1]
                        temp = 1
                        for i in range(1, n + 1):
                            if matrix[x - i][y] != '1' or matrix[x][y - i] != '1':
                                break
                            temp += 1
                        sumMatrix[x][y] = temp
                        res = max(res, temp)
                    else:
                        sumMatrix[x][y] = 1
                        res = max(res, 1)
        for t in sumMatrix:
            print(t)
        return res ** 2


print(Solution().maximalSquare([["1", "0", "1", "0", "0"],
                                ["1", "0", "1", "1", "1"],
                                ["1", "1", "1", "1", "1"],
                                ["1", "0", "0", "1", "0"]]))  # 4

print(Solution().maximalSquare(
    [["0", "0", "0", "1"],
     ["1", "1", "0", "1"],
     ["1", "1", "1", "1"],
     ["0", "1", "1", "1"],
     ["0", "1", "1", "1"]]))  # 9
