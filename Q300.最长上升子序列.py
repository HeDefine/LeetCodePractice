#!/usr/bin/env python3

# https://leetcode-cn.com/problems/longest-increasing-subsequence
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#
# 说明:
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
#
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        orders = [0] * len(nums)
        for idx, val in enumerate(nums):
            for idx2 in range(idx):
                if nums[idx2] < val:
                    orders[idx] = max(orders[idx], orders[idx2])
            orders[idx] += 1
        return max(orders) if len(orders) > 0 else 0


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
