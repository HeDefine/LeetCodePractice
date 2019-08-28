#!/usr/bin/env python3

# https://leetcode-cn.com/problems/peak-index-in-a-mountain-array
# 我们把符合下列属性的数组 A 称作山脉：
# 1. A.length >= 3
# 2. 存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
#
# 给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。
#
# 示例 1：
# 输入：[0,1,0]
# 输出：1
#
# 示例 2：
# 输入：[0,2,1,0]
# 输出：1
#
# 提示：
# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A 是如上定义的山脉


class Solution:
    def peakIndexInMountainArray(self, A: [int]) -> int:
        minIdx = 0
        maxIdx = len(A) - 1
        while minIdx <= maxIdx:
            mid = (minIdx + maxIdx) // 2
            if A[mid - 1] < A[mid] > A[mid + 1]:
                return mid
            elif A[mid] <= A[mid + 1]:
                minIdx = mid
            elif A[mid] <= A[mid - 1]:
                maxIdx = mid
        return 0


print(Solution().peakIndexInMountainArray([0, 1, 0]))  # 1
print(Solution().peakIndexInMountainArray([0, 2, 1, 0]))  # 1
print(Solution().peakIndexInMountainArray([3, 4, 5, 1]))
print(Solution().peakIndexInMountainArray([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
