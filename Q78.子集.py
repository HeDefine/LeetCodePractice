#!/usr/bin/env python3

# https://leetcode-cn.com/problems/subsets
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
#
# 示例:
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution:
    def subsets(self, nums: [int]) -> [[int]]:

        def cover(cur: [int], idx):
            res.append(cur)
            for i in range(idx, len(nums)):
                cover(cur + [nums[i]], i + 1)

        res = list()
        cover([], 0)
        return res


print(Solution().subsets([1, 2, 3]))
