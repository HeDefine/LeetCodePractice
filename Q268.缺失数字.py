#!/usr/bin/env python3

# https://leetcode-cn.com/problems/missing-number
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
#
# 示例 1:
# 输入: [3,0,1]
# 输出: 2
#
# 示例 2:
# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8


class Solution:
    # 用set 来解决
    def missingNumber1(self, nums: [int]) -> int:
        set0 = set(range(len(nums) + 1))
        set1 = set(nums)
        result = set0 - set1
        return result.pop()
    # 用和的方式来解决
    def missingNumber2(self, nums: [int]) -> int:
        sum0 = 0
        sum1 = 0
        for idx, num in enumerate(nums):
            sum0 += idx
            sum1 += num
        return sum0 + len(nums) - sum1


print(Solution().missingNumber([3, 0, 1]))  # 2
print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
