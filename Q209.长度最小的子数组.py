#!/usr/bin/env python3

# https://leetcode-cn.com/problems/minimum-size-subarray-sum
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
#
# 示例: 
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 进阶:
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。


class Solution:
    def minSubArrayLen(self, s: int, nums: [int]) -> int:
        res = list()
        cur = list()
        sumV = 0
        for num in nums:
            sumV += num
            cur.append(num)
            if sumV >= s:
                while sumV >= s:
                    if sumV - cur[0] < s:
                        break
                    sumV -= cur.pop(0)
                if len(res) == 0 or len(cur) <= len(res):
                    res = cur[:]
        return len(res)


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2
print(Solution().minSubArrayLen(4, [1, 4, 4]))  # 1
print(Solution().minSubArrayLen(15, [1, 2, 3, 4, 5]))  # 5
print(Solution().minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))  # 2
