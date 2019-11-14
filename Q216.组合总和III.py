#!/usr/bin/env python3

# https://leetcode-cn.com/problems/combination-sum-iii
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 说明：
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
#
# 示例 1:
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
#
# 示例 2:
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]


class Solution:
    def combinationSum3(self, k: int, n: int) -> [[int]]:
        def recursion(cur: [int], allPurpose: [int], sumV: int, num: int):
            if num == 0 and sumV == 0:
                res.append(cur)
            elif num > 0 and sumV > 0:
                for idx, pur in enumerate(allPurpose):
                    if sumV - pur >= 0:
                        recursion(cur + [pur], allPurpose[idx + 1:], sumV - pur, num - 1)

        res = list()
        recursion([], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], n, k)
        return res


print(Solution().combinationSum3(3, 7))  # [1,2,4]
print(Solution().combinationSum3(3, 9))  # [[1,2,6],[1,3,5],[2,3,4]]
