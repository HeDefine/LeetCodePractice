#!/usr/bin/env python3

# https://leetcode-cn.com/problems/rotate-image
# 给定一个 n × n 的二维矩阵表示一个图像。
# 将图像顺时针旋转 90 度。
# 说明：
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。


class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        n = len(matrix)
        flag = 0
        for row in range(flag, n // 2):
            for col in range(flag, n - 1 - flag):
                matrix[row][col], matrix[col][n - 1 - row], matrix[n - 1 - row][n - 1 - col], matrix[n - 1 - col][row] \
                    = matrix[n - 1 - col][row], matrix[row][col], matrix[col][n - 1 - row], matrix[n - 1 - row][
                    n - 1 - col]
            flag += 1


# Solution().rotate([[1, 2], [2, 3]])

Solution().rotate(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]


Solution().rotate([
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
])
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
