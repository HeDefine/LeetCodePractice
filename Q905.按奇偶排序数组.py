#!/usr/bin/env python3

# https://leetcode-cn.com/problems/sort-array-by-parity
# 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
# 你可以返回满足此条件的任何数组作为答案。
#
# 示例：
# 输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
#
# 提示：
# 1. 1 <= A.length <= 5000
# 2. 0 <= A[i] <= 5000
#

class Solution:
    def sortArrayByParity(self, A: [int]) -> [int]:
        tempA = list()
        tempB = list()
        for n in A:
            if n % 2 == 0:
                tempA.append(n)
            else:
                tempB.append(n)
        return tempA + tempB


print(Solution().sortArrayByParity([3, 1, 2, 4]))  # [2,4,3,1]
