#!/usr/bin/env python3

# https://leetcode-cn.com/problems/set-matrix-zeroes
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#
# 进阶:
# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？


class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        matrix.insert(0, [0] * (len(matrix[0]) + 1))
        for x in range(1, len(matrix)):
            flag = False
            for y in range(len(matrix[x])):
                val = matrix[x][y]
                if val == 0:
                    matrix[0][y + 1] = 1
                    flag = True
            matrix[x] = [1 if flag else 0] + matrix[x]

        for x in range(1, len(matrix)):
            for y in range(1, len(matrix[x])):
                if matrix[0][y] == 1 or matrix[x][0] == 1:
                    matrix[x][y] = 0
            matrix[x].pop(0)
        matrix.pop(0)


t = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
Solution().setZeroes(t)
print(t)

print(Solution().setZeroes([
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]]
))
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
