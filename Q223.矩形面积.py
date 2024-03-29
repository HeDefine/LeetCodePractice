#!/usr/bin/env python3

# https://leetcode-cn.com/problems/rectangle-area
# 在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。
# 每个矩形由其左下顶点和右上顶点坐标表示，如图所示。
#
# 示例:
# 输入: -3, 0, 3, 4, 0, -1, 9, 2
# 输出: 45
# 说明: 假设矩形面积不会超出 int 的范围


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = abs((A - C) * (B - D))
        area2 = abs((E - G) * (F - H))
        overArea = max(0, min(C, G) - max(A, E)) * max(0, min(D, H) - max(B, F))
        return area1 + area2 - overArea


print(Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
