#!/usr/bin/env python3

# https://leetcode-cn.com/problems/number-of-boomerangs
# 给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
# 找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。
#
# 示例:
# 输入:
# [[0,0],[1,0],[2,0]]
# 输出:
# 2
#
# 解释:
# 两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]


class Solution:
    def numberOfBoomerangs(self, points: [[int]]) -> int:
        result = 0
        for i in points:
            temp = {}
            for j in points:
                d = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
                temp[d] = temp.get(d, 0) + 1
            for v in list(temp.values()):
                if v >= 2:
                    result += v * (v - 1)
        return result


print(Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))  # 2
