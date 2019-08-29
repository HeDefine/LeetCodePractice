#!/usr/bin/env python3

# https://leetcode-cn.com/problems/projection-area-of-3d-shapes
# 在 N * N 的网格中，我们放置了一些与 x，y，z 三轴对齐的 1 * 1 * 1 立方体。
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
# 现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。
# 投影就像影子，将三维形体映射到一个二维平面上。
# 在这里，从顶部、前面和侧面看立方体时，我们会看到“影子”。
# 返回所有三个投影的总面积。
#  
# 示例 1：
# 输入：[[2]]
# 输出：5
#
# 示例 2：
# 输入：[[1,2],[3,4]]
# 输出：17
# 解释：
# 这里有该形体在三个轴对齐平面上的三个投影(“阴影部分”)。


class Solution:
    def projectionArea(self, grid: [[int]]) -> int:
        res1 = 0  # 俯视图
        res2 = 0  # 主视图
        res3 = 0  # 左视图

        for l in grid:
            res1 += len([v for v in l if v > 0])
            res2 += max(l)

        for l in zip(*grid):
            res3 += max(l)

        return res1 + res2 + res3


print(Solution().projectionArea([[2]]))  # 5
print(Solution().projectionArea([[1, 2], [3, 4]]))  # 17
