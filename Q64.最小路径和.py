#!/usr/bin/env python3

# https://leetcode-cn.com/problems/minimum-path-sum
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。


class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for x, line in enumerate(grid):
            for y, val in enumerate(line):
                if x - 1 >= 0 and y - 1 >= 0:
                    val1 = grid[x - 1][y]
                    val2 = grid[x][y - 1]
                    grid[x][y] = min(val1, val2) + val
                elif x - 1 >= 0:
                    grid[x][y] = val + grid[x - 1][y]
                elif y - 1 >= 0:
                    grid[x][y] = val + grid[x][y - 1]
        return grid[-1][-1]


print(Solution().minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
