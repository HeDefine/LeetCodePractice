#!/usr/bin/env python3

# https://leetcode-cn.com/problems/island-perimeter
# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
# 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
#
# 示例 :
# 输入:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# 输出: 16
# 解释: 它的周长是下面图片中的 16 个黄色的边：


class Solution:
    def islandPerimeter(self, grid: [[int]]) -> int:
        islandNum = 0
        unionLand = 0
        for row, eachLine in enumerate(grid):
            for col, num in enumerate(eachLine):
                if num == 1:
                    islandNum += 1
                    if row - 1 >= 0 and grid[row - 1][col] == 1:
                        unionLand += 1
                    if row + 1 < len(grid) and grid[row + 1][col] == 1:
                        unionLand += 1
                    if col - 1 >= 0 and eachLine[col - 1] == 1:
                        unionLand += 1
                    if col + 1 < len(eachLine) and eachLine[col + 1] == 1:
                        unionLand += 1
        return islandNum * 4 - unionLand


print(Solution().islandPerimeter([[1], [0]]))
print(Solution().islandPerimeter([[0, 1, 0, 0],
                                  [1, 1, 1, 0],
                                  [0, 1, 0, 0],
                                  [1, 1, 0, 0]]))  # 16
