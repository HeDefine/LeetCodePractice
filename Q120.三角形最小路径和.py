#!/usr/bin/env python3

# https://leetcode-cn.com/problems/triangle
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 例如，给定三角形：
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
# 说明：
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。


class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:
        minV = 0
        for row, line in enumerate(triangle):
            minV = line[0]
            if row == 0:
                continue
            for idx, val in enumerate(line):
                if idx == 0:
                    triangle[row][idx] = triangle[row - 1][0] + val
                    minV = triangle[row][idx]
                elif idx == row:
                    triangle[row][idx] = triangle[row - 1][idx - 1] + val
                else:
                    triangle[row][idx] = min(triangle[row - 1][idx], triangle[row - 1][idx - 1]) + val

                if minV > triangle[row][idx]:
                    minV = triangle[row][idx]
            print(triangle, minV)
        return minV


print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
#       [-1]
#     [2,   3]
#    [1, -1, -3]
# print(Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]]))
