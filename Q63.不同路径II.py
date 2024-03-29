#!/usr/bin/env python3

# https://leetcode-cn.com/problems/unique-paths-ii
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
#
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        res = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        if obstacleGrid[0][0] != 1:
            res[0][0] = 1
        for x, line in enumerate(obstacleGrid):
            for y, val in enumerate(line):
                if val == 1:
                    continue
                if x - 1 >= 0:
                    res[x][y] += res[x - 1][y]
                if y - 1 >= 0:
                    res[x][y] += res[x][y - 1]
        return res[-1][-1]


print(Solution().uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))  # 2
