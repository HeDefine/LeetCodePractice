#!/usr/bin/env python3

# https://leetcode-cn.com/problems/spiral-matrix
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
#
# 示例 2:
# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        res = list()
        flag = 0
        while len(matrix) > 0:
            if flag % 4 == 0:
                # 正序第一行
                res += matrix.pop(0)
            elif flag % 4 == 1:
                # 正序最后一列
                idx = 0
                while idx < len(matrix):
                    res.append(matrix[idx].pop(-1))
                    if len(matrix[idx]) == 0:
                        matrix.pop(idx)
                        continue
                    idx += 1

            elif flag % 4 == 2:
                # 逆序最后一行
                res += matrix.pop(-1)[::-1]
            elif flag % 4 == 3:
                # 逆序第一列
                idx = len(matrix) - 1
                while idx >= 0:
                    res.append(matrix[idx].pop(0))
                    if len(matrix[idx]) == 0:
                        matrix.pop(idx)
                    idx -= 1

            flag += 1
        return res


print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1,2,3,6,9,8,7,4,5]
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # [1,2,3,4,8,12,11,10,9,5,6,7]
print(Solution().spiralOrder(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))  # [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
print(Solution().spiralOrder([[7], [9], [6]]))
print(Solution().spiralOrder([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]))
print(Solution().spiralOrder([[2,5],[8,4],[0,-1]]))
# 1，2，3，4
# 5，6，7，8
# 9，10，11，12
# 13，14，15，16
