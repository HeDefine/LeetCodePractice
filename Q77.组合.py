#!/usr/bin/env python3

# https://leetcode-cn.com/problems/combinations
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


class Solution:
    def combine(self, n: int, k: int) -> [[int]]:

        def cover(cur: [int], curV):
            if len(cur) == k:
                res.append(cur[:])
            elif len(cur) > k:
                return
            for i in range(curV, n + 1):
                cover(cur + [i], i + 1)

        res = list()
        cover([], 1)
        return res


print(Solution().combine(4, 2))
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
