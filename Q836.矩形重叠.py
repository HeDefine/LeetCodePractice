#!/usr/bin/env python3

# https://leetcode-cn.com/problems/rectangle-overlap
# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
# 如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
# 给出两个矩形，判断它们是否重叠并返回结果。
#
# 示例 1：
# 输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# 输出：true
#
# 示例 2：
# 输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# 输出：false
#
# 说明：
# 两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
# 矩形中的所有坐标都处于 -10^9 和 10^9 之间。


class Solution:
    def isRectangleOverlap(self, rec1: [int], rec2: [int]) -> bool:
        if rec1[0] >= rec2[2] or rec2[0] >= rec1[2] or rec1[1] >= rec2[3] or rec2[1] >= rec1[3]:
            return False
        return True


print(Solution().isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]))  # True
print(Solution().isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]))  # False
print(Solution().isRectangleOverlap([7, 8, 13, 15], [10, 8, 12, 20]))  # True
# (7,8) (7,15) (13,8) (13,15)           (10, 8) (10, 20) (12, 8) (12, 20)
print(Solution().isRectangleOverlap([5, 15, 8, 18], [0, 3, 7, 9]))  # False
# (5,15) (5,18) (8, 15) (8 ,18)             (0, 3) (0, 9) (7, 3) (7, 9)
