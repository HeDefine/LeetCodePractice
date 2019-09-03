#!/usr/bin/env python3

# https://leetcode-cn.com/problems/squares-of-a-sorted-array
# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
#
# 示例 1：
# 输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
#
# 示例 2：
# 输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#
# 提示：
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A 已按非递减顺序排序。


class Solution:
    def sortedSquares(self, A: [int]) -> [int]:
        first = 0
        last = len(A) - 1

        res = list()
        while first <= last:
            if abs(A[last]) > abs(A[first]):
                res.append(A[last] ** 2)
                last -= 1
            elif abs(A[last]) < abs(A[first]):
                res.append(A[first] ** 2)
                first += 1
            else:
                if first == last:
                    res.append(A[first] ** 2)
                else:
                    res.append(A[first] ** 2)
                    res.append(A[last] ** 2)
                first += 1
                last -= 1
        res.reverse()
        return res


print(Solution().sortedSquares([-4, -1, 0, 3, 10]))  # [0,1,9,16,100]
print(Solution().sortedSquares([-7, -3, 2, 3, 11]))  # [4,9,9,49,121]
