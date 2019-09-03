#!/usr/bin/env python3

# https://leetcode-cn.com/problems/largest-perimeter-triangle
# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
# 如果不能形成任何面积不为零的三角形，返回 0。
#
# 示例 1：
# 输入：[2,1,2]
# 输出：5
#
# 示例 2：
# 输入：[1,2,1]
# 输出：0
#
# 示例 3：
# 输入：[3,2,3,4]
# 输出：10
#
# 示例 4：
# 输入：[3,6,2,3]
# 输出：8
#  
# 提示：
# 3 <= A.length <= 10000
# 1 <= A[i] <= 10^6


class Solution:
    def largestPerimeter(self, A: [int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            for j in range(i + 1, len(A) - 1):
                for o in range(j + 1, len(A)):
                    if A[i] < A[j] + A[o]:
                        return A[i] + A[j] + A[o]
                    else:
                        break
        return 0


print(Solution().largestPerimeter([2, 1, 2]))  # 5
print(Solution().largestPerimeter([1, 2, 1]))  # 0
print(Solution().largestPerimeter([3, 2, 3, 4]))  # 10
print(Solution().largestPerimeter([3, 6, 2, 3]))  # 8
