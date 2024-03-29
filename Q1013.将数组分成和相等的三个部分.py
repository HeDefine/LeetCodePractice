#!/usr/bin/env python3

# https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum
# 给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
#
# 形式上，如果我们可以找出索引 i+1 < j 
# 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 
# 就可以将数组三等分。
#
# 示例 1：
# 输出：[0,2,1,-6,6,-7,9,1,2,0,1]
# 输出：true
# 解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#
# 示例 2：
# 输入：[0,2,1,-6,6,7,9,-1,2,0,1]
# 输出：false
#
# 示例 3：
# 输入：[3,3,6,5,-2,2,5,1,-9,4]
# 输出：true
# 解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#
# 提示：
# 1. 3 <= A.length <= 50000
# 2. -10000 <= A[i] <= 10000


class Solution:
    def canThreePartsEqualSum(self, A: [int]) -> bool:
        sumA = sum(A)
        if sumA % 3 != 0:
            return False
        eachSum = sum(A) // 3

        headIdx = -1
        footIdx = len(A)
        sumHead = 0
        sumFoot = 0
        while headIdx < footIdx:
            if sumHead != eachSum:
                headIdx += 1
                sumHead += A[headIdx]
            if sumFoot != eachSum:
                footIdx -= 1
                sumFoot += A[footIdx]
            if sumHead == sumFoot == eachSum:
                break
        return headIdx < footIdx


print(Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))  # True
print(Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))  # False
print(Solution().canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))  # True
