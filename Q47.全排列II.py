#!/usr/bin/env python3

# https://leetcode-cn.com/problems/permutations-ii
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        def cover(current: [int], allNum: [int]):
            if len(allNum) == 0:
                res.append(current)
            else:
                for idx, val in enumerate(allNum):
                    if idx > 0 and allNum[idx - 1] == val:
                        continue
                    cover(current + [val], allNum[:idx] + allNum[idx + 1:])

        nums.sort()
        res = list()
        cover([], nums)
        return res


print(Solution().permuteUnique([1, 1, 2]))
