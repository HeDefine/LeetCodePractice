#!/usr/bin/env python3

# https://leetcode-cn.com/problems/spiral-matrix-ii
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        res = [[0] * n for _ in range(n)]
        val = 0
        startCol = 0
        endCol = n
        startRow = 0
        endRow = n
        while val < n ** 2:
            # 顺行
            for col in range(startCol, endCol):
                val += 1
                res[startRow][col] = val
            startRow += 1
            endCol -= 1

            # 顺列
            for row in range(startRow, endRow):
                val += 1
                res[row][endCol] = val
            endRow -= 1

            # 逆行
            for col in range(endCol - 1, startCol - 1, -1):
                val += 1
                res[endRow][col] = val

            # 逆列
            for row in range(endRow - 1, startRow - 1, -1):
                val += 1
                res[row][startCol] = val
            startCol += 1

        return res


print(Solution().generateMatrix(1))
print(Solution().generateMatrix(2))
print(Solution().generateMatrix(3))
print(Solution().generateMatrix(4))
print(Solution().generateMatrix(5))
# print(Solution().generateMatrix(6))
