#!/usr/bin/env python3

# https://leetcode-cn.com/problems/magic-squares-in-grid
# 3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
# 给定一个由整数组成的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。
#
# 示例：
# 输入: [[4,3,8,4],
#       [9,5,1,9],
#       [2,7,6,2]]
# 输出: 1
#
# 解释:
# 下面的子矩阵是一个 3 x 3 的幻方：
# 438
# 951
# 276
#
# 而这一个不是：
# 384
# 519
# 762
#
# 总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
# 提示:
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# 0 <= grid[i][j] <= 15


class Solution:
    def numMagicSquaresInside(self, grid: [[int]]) -> int:
        res = 0
        for r in range(len(grid) - 2):
            for c in range(len(grid[r]) - 2):
                temp = [
                    [grid[r][c], grid[r][c + 1], grid[r][c + 2]],
                    [grid[r + 1][c], grid[r + 1][c + 1], grid[r + 1][c + 2]],
                    [grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2]]
                ]
                set0 = set()
                set0 = set0.union(temp[0], temp[1], temp[2])
                if len(set0) < 9 or max(set0) > 9:
                    continue

                rowSum = -1
                if sum(temp[0]) == sum(temp[1]) == sum(temp[2]):
                    rowSum = sum(temp[0])
                else:
                    continue
                columnSum = -1
                if temp[0][0] + temp[1][0] + temp[2][0] == temp[0][1] + temp[1][1] + temp[2][1] == temp[0][2] + temp[1][
                    2] + temp[2][2]:
                    columnSum = temp[0][0] + temp[1][0] + temp[2][0]
                else:
                    continue

                if temp[0][0] + temp[1][1] + temp[2][2] == temp[0][2] + temp[1][1] + temp[2][0] == rowSum == columnSum:
                    res += 1
                else:
                    continue
        return res


print(Solution().numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))  # 1
print(Solution().numMagicSquaresInside([[2, 7, 6], [1, 5, 9], [4, 3, 8]]))  # 0
print(Solution().numMagicSquaresInside([[5, 5, 5], [5, 5, 5], [5, 5, 5]]))  # 0
