#!/usr/bin/env python3

# https://leetcode-cn.com/problems/search-a-2d-matrix
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。

class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        rowLst = 0
        rowRst = len(matrix) - 1
        if rowLst > rowRst:
            return False
        while rowLst <= rowRst:
            mid = (rowLst + rowRst) // 2
            if len(matrix[mid]) == 0:
                return False
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                rowLst = mid + 1
            elif matrix[mid][0] > target:
                rowRst = mid - 1

        t = matrix[rowRst]
        colLst = 0
        colRst = len(t) - 1
        while colLst <= colRst:
            mid = (colLst + colRst) // 2
            if t[mid] == target:
                return True
            elif t[mid] < target:
                colLst = mid + 1
            elif t[mid] > target:
                colRst = mid - 1
        return False


print(Solution().searchMatrix(
    matrix=[
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ],
    target=30
))  # True

print(Solution().searchMatrix(
    matrix=[
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ],
    target=13
))  # False
