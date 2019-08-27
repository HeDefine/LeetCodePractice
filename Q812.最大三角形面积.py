#!/usr/bin/env python3

# https://leetcode-cn.com/problems/largest-triangle-area
# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
# 示例:
# 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# 输出: 2
# 解释:
# 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
#
# 注意:
# 3 <= points.length <= 50.
# 不存在重复的点。
#  -50 <= points[i][j] <= 50.
# 结果误差值在 10^-6 以内都认为是正确答案。


class Solution:
    def largestTriangleArea(self, points: [[int]]) -> float:
        maxArea = 0
        for idx1 in range(len(points) - 2):
            x = points[idx1]
            for idx2 in range(idx1 + 1, len(points) - 1):
                y = points[idx2]
                for idx3 in range(idx2 + 1, len(points)):
                    z = points[idx3]
                    area = (1 / 2) * (x[0] * y[1] + y[0] * z[1] + z[0] * x[1] - x[0] * z[1] - y[0] * x[1] - z[0] * y[1])
                    maxArea = max(maxArea, abs(area))
        return maxArea


print(Solution().largestTriangleArea([[0, 0], [0, 1], [1, 0]]))  # 2
print(Solution().largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))  # 2
