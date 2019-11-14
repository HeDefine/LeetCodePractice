#!/usr/bin/env python3

# https://leetcode-cn.com/problems/house-robber-ii
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
# 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例 1:
# 输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#
# 示例 2:
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。


class Solution:
    def rob(self, nums: [int]) -> int:

        sumList1 = [0] * len(nums)
        sumList2 = [0] * len(nums)
        for idx, val in enumerate(nums):
            if idx >= 1:
                pur1 = sumList1[idx - 2] if idx - 2 >= 0 else 0
                pur2 = sumList1[idx - 3] if idx - 3 >= 0 else 0
                sumList1[idx] = max(sumList1[idx - 1], val + max(pur1, pur2))

            if idx < len(nums) - 1:
                pur3 = sumList2[idx - 2] if idx - 2 >= 0 else 0
                pur4 = sumList2[idx - 3] if idx - 3 >= 0 else 0
                sumList2[idx] = max(sumList2[idx - 1], val + max(pur3, pur4))
                print(sumList2)

        if len(nums) == 1:
            return nums[0]
        return max(sumList1[-1] if len(sumList1) > 0 else 0, sumList2[-2] if len(sumList2) > 1 else 0)


# print(Solution().rob([2, 3, 2]))
# print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([2, 7, 9, 3, 1]))
# print(Solution().rob([1]))
