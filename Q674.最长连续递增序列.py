#!/usr/bin/env python3

# https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence
# 给定一个未经排序的整数数组，找到最长且连续的的递增序列。
#
# 示例 1:
# 输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
#
# 示例 2:
# 输入: [2,2,2,2,2]
# 输出: 1
# 解释: 最长连续递增序列是 [2], 长度为1。


class Solution:
    def findLengthOfLCIS(self, nums: [int]) -> int:
        res = 0
        count = 0
        for idx, n in enumerate(nums):
            count += 1
            if idx + 1 < len(nums) and n >= nums[idx + 1]:
                res = max(res, count)
                count = 0
        res = max(res, count)
        return res


print(Solution().findLengthOfLCIS([1, 3, 5, 4, 7]))  # 3
print(Solution().findLengthOfLCIS([2, 2, 2, 2, 2]))  # 1
print(Solution().findLengthOfLCIS([1, 3, 5, 7]))  # 4
