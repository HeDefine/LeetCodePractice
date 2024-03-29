#!/usr/bin/env python3

# https://leetcode-cn.com/problems/search-a-2d-matrix-ii
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
#
# 示例:
# 现有矩阵 matrix 如下：
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。
# 给定 target = 20，返回 false。


class Solution:
    def searchMatrix(self, matrix, target):
        row, col = len(matrix) - 1, 0
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                col += 1
            else:
                row -= 1
        return False


print(Solution().searchMatrix([
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
], 5))  # True

print(Solution().searchMatrix([
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
], 20))  # False
