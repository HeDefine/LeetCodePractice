#!/usr/bin/env python3

# https://leetcode-cn.com/problems/summary-ranges
# 给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。
# 示例 1:
# 输入: [0,1,2,4,5,7]
# 输出: ["0->2","4->5","7"]
# 解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
#
# 示例 2:
# 输入: [0,2,3,4,6,8,9]
# 输出: ["0","2->4","6","8->9"]
# 解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。


class Solution:
    def summaryRanges(self, nums: [int]) -> [str]:
        start = None
        res = list()
        for idx, val in enumerate(nums):
            if start is None:
                start = val
            if idx + 1 < len(nums) and nums[idx + 1] - val != 1 or idx + 1 == len(nums):
                if start == val:
                    res.append(str(val))
                else:
                    res.append(str(start) + '->' + str(val))
                start = None
        return res


print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))  # ["0->2","4->5","7"]
print(Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]))  # ["0","2->4","6","8->9"]
