#!/usr/bin/env python3

# https://leetcode-cn.com/problems/combination-sum
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
#
# 示例 1:
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
#
# 示例 2:
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]


class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        def coverAllPurpose(nums: [int], t: int, currentList: [int]):
            for val in nums:
                if len(currentList) == 0 or val >= currentList[-1]:
                    if val == t:
                        res.append(currentList + [val])
                    elif val < t:
                        coverAllPurpose(nums, t - val, currentList + [val])

        res = list()
        coverAllPurpose(candidates, target, [])
        return res


print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))  # [[7],[2,2,3]]
print(Solution().combinationSum(candidates=[2, 3, 5], target=8))  # [[2,2,2,2],[2,3,3],[3,5]]
