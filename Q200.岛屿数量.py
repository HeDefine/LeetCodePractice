#!/usr/bin/env python3

# https://leetcode-cn.com/problems/number-of-islands
# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#
# 示例 1:
# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
#
# 示例 2:
# 输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3

class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        def spread(x, y):
            if grid[x][y] == '1' and not visited[x][y]:
                visited[x][y] = True
                if x - 1 >= 0:
                    spread(x - 1, y)
                if x + 1 < len(grid):
                    spread(x + 1, y)
                if y - 1 >= 0:
                    spread(x, y - 1)
                if y + 1 < len(grid[0]):
                    spread(x, y + 1)

        res = 0
        visited = [[False] * len(grid[0]) for i in range(len(grid))]
        for i, line in enumerate(grid):
            for j, val in enumerate(line):
                if val == '1' and not visited[i][j]:
                    res += 1
                    spread(i, j)
        return res


print(Solution().numIslands(
    [["1", "1", "1", "1", "0"],
     ["1", "1", "0", "1", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "0", "0", "0"]]))  # 1

print(Solution().numIslands([["1", "1", "1"],
                             ["0", "1", "0"],
                             ["1", "1", "1"]]))  # 1

print(Solution().numIslands([["1", "1", "1", "1", "1", "1"],
                             ["1", "0", "0", "0", "0", "1"],
                             ["1", "0", "1", "1", "0", "1"],
                             ["1", "0", "0", "0", "0", "1"],
                             ["1", "1", "1", "1", "1", "1"]]))
