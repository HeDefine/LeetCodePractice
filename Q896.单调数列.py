#!/usr/bin/env python3

# https://leetcode-cn.com/problems/monotonic-array
# 如果数组是单调递增或单调递减的，那么它是单调的。
# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
# 当给定的数组 A 是单调数组时返回 true，否则返回 false。
#
# 提示：
# 1. 1 <= A.length <= 50000
# 2. -100000 <= A[i] <= 100000


class Solution:
    def isMonotonic(self, A: [int]) -> bool:
        flag = 0
        for idx, val in enumerate(A):
            if idx > 0 and A[idx - 1] < A[idx]:
                if flag == 0 or flag == 1:
                    flag = 1
                else:
                    return False
            if idx > 0 and A[idx - 1] > A[idx]:
                if flag == 0 or flag == -1:
                    flag = -1
                else:
                    return False
        return True


print(Solution().isMonotonic([1, 2, 2, 3]))  # True
print(Solution().isMonotonic([6, 5, 4, 4]))  # True
print(Solution().isMonotonic([1, 3, 2]))  # False
print(Solution().isMonotonic([1, 2, 4, 5]))  # True
print(Solution().isMonotonic([1, 1, 1]))  # True
print(Solution().isMonotonic([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]))  # False
