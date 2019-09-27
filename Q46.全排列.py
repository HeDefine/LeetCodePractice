#!/usr/bin/env python3

# https://leetcode-cn.com/problems/permutations
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例:
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        def cover(current: [int], allNum: [int]):
            if len(allNum) == 0:
                res.append(current)
            else:
                for idx, val in enumerate(allNum):
                    cover(current + [val], allNum[:idx] + allNum[idx + 1:])

        res = list()
        cover([], nums)
        return res


print(Solution().permute([1, 2, 3]))
