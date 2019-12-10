#!/usr/bin/env python3

# https://leetcode-cn.com/problems/range-sum-query-2d-immutable
# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。
# 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
# 给定 matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
#
# 说明:
# 你可以假设矩阵不可变。
# 会多次调用 sumRegion 方法。
# 你可以假设 row1 ≤ row2 且 col1 ≤ col2。


class NumMatrix:

    def __init__(self, matrix: [[int]]):
        self.sumRectangle = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i, line in enumerate(matrix):
            sumV = 0
            for j, val in enumerate(line):
                sumV += val
                if i > 0:
                    self.sumRectangle[i][j] = self.sumRectangle[i - 1][j] + sumV
                else:
                    self.sumRectangle[i][j] = sumV
        print(self.sumRectangle)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sumV = self.sumRectangle[row2][col2]
        if row1 > 0:
            sumV -= self.sumRectangle[row1 - 1][col2]
        if col1 > 0:
            sumV -= self.sumRectangle[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            sumV += self.sumRectangle[row1 - 1][col1 - 1]
        return sumV


obj = NumMatrix([
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
])
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))
