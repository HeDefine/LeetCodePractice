#!/usr/bin/env python3

# https://leetcode-cn.com/problems/valid-boomerang
# 回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。
# 给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。
#
# 示例 1：
# 输入：[[1,1],[2,3],[3,2]]
# 输出：true
#
# 示例 2：
# 输入：[[1,1],[2,2],[3,3]]
# 输出：false
#
# 提示：
# points.length == 3
# points[i].length == 2
# 0 <= points[i][j] <= 100


class Solution:
    def isBoomerang(self, points: [[int]]) -> bool:
        A = points[0]
        B = points[1]
        C = points[2]
        if A == B or B == C or A == C:
            return False

        # 求AB组成的一条直线
        # y1 = kx1 + b                      k = (y1 - y2) / (x1 - x2)
        #                       =>
        # y2 = kx2 + b                      b = y1 - (y1 - y2)/(x1 - x2) * x1
        if A[0] != B[0]:
            k = (A[1] - B[1]) / (A[0] - B[0])
            b = A[1] - (A[1] - B[1]) / (A[0] - B[0]) * A[0]
            if C[1] == k * C[0] + b:
                return False
            return True
        else:
            return C[0] != A[0]


# print(Solution().isBoomerang([[1, 1], [2, 3], [3, 2]]))  # True
# print(Solution().isBoomerang([[1, 1], [2, 2], [3, 3]]))  # False
# print(Solution().isBoomerang([[0, 0], [0, 2], [2, 1]]))  # True
# print(Solution().isBoomerang([[1, 0], [1, 1], [2, 0]]))  # True
print(Solution().isBoomerang([[1, 1], [1, 2], [0, 0]]))  # True
