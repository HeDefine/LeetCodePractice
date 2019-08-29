#!/usr/bin/env python3

# https://leetcode-cn.com/problems/surface-area-of-3d-shapes
# 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
# 请你返回最终形体的表面积。
#
# 示例 1：
# 输入：[[2]]
# 输出：10
#
# 示例 2：
# 输入：[[1,2],[3,4]]
# 输出：34
#
# 示例 3：
# 输入：[[1,0],[0,2]]
# 输出：16
#
# 示例 4：
# 输入：[[1,1,1],[1,0,1],[1,1,1]]
# 输出：32
#
# 示例 5：
# 输入：[[2,2,2],[2,1,2],[2,2,2]]
# 输出：46
#
# 提示：
# 1. 1 <= N <= 50
# 2. 0 <= grid[i][j] <= 50


class Solution:
    def surfaceArea(self, grid: [[int]]) -> int:
        allS = 0
        repeatView = 0
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                allS += 6 * val
                if y > 0:
                    repeatView += min(val, row[y - 1])  # 同一个行重叠的面积
                if x > 0 and y < len(grid[x - 1]):
                    repeatView += min(val, grid[x - 1][y])  # 同一个列重叠的面积
                if val > 1:
                    repeatView += (val - 1)  # 同一个位置叠加的重叠的面积
        return allS - repeatView * 2


print(Solution().surfaceArea([[2]]))  # 10
print(Solution().surfaceArea([[1, 2], [3, 4]]))  # 34
print(Solution().surfaceArea([[1, 0], [0, 2]]))  # 16
print(Solution().surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # 32
print(Solution().surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))  # 46
