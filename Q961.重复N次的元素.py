#!/usr/bin/env python3

# 链接：https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array
# 在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
# 返回重复了 N 次的那个元素。
#
# 示例 1：
# 输入：[1,2,3,3]
# 输出：3
#
# 示例 2：
# 输入：[2,1,2,5,3,2]
# 输出：2
#
# 示例 3：
# 输入：[5,1,5,2,5,3,5,4]
# 输出：5
#
# 提示：
# 4 <= A.length <= 10000
# 0 <= A[i] < 10000
# A.length 为偶数


class Solution:
    def repeatedNTimes(self, A: [int]) -> int:
        temp = dict()
        for n in A:
            temp[n] = temp.get(n, 0) + 1
        for k, v in temp.items():
            if v == len(A) // 2:
                return k
        return 0


print(Solution().repeatedNTimes([1, 2, 3, 3]))  # 3
print(Solution().repeatedNTimes([2, 1, 2, 5, 3, 2]))  # 2
print(Solution().repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))  # 5
print(Solution().repeatedNTimes([9, 5, 3, 3]))  # 3
