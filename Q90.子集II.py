#!/usr/bin/env python3

# https://leetcode-cn.com/problems/subsets-ii
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
#
# 示例:
# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        def cover(cur: [int], idx):
            res.append(cur)
            for i in range(idx, len(nums)):
                if i == idx or nums[i] != nums[i - 1]:
                    cover(cur + [nums[i]], i + 1)

        res = list()
        nums.sort()
        cover([], 0)
        return res


print(Solution().subsetsWithDup([1, 2, 2]))
