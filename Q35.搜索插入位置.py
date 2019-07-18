#!/usr/bin/env python3

# https://leetcode-cn.com/problems/search-insert-position
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
#
# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2
#
# 示例 2:
# 输入: [1,3,5,6], 2
# 输出: 1
#
# 示例 3:
# 输入: [1,3,5,6], 7
# 输出: 4
#
# 示例 4:
# 输入: [1,3,5,6], 0
# 输出: 0


class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        minIdx = 0
        maxIdx = len(nums) - 1
        if target <= nums[minIdx]:
            return 0
        if target > nums[maxIdx]:
            return maxIdx + 1
        while minIdx <= maxIdx:
            midIdx = (minIdx + maxIdx) // 2
            if nums[midIdx] < target <= nums[midIdx + 1]:
                return midIdx + 1
            elif target <= nums[midIdx]:
                maxIdx = midIdx
            elif target > nums[midIdx + 1]:
                minIdx = midIdx + 1

    def searchInsert2(self, nums: [int], target: int) -> int:
        for idx, num in enumerate(nums):
            if target <= num:
                return idx
        return len(nums)

print(Solution().searchInsert2([1, 3, 5, 6], 5))
print(Solution().searchInsert2([1, 3, 5, 6], 2))
print(Solution().searchInsert2([1, 3, 5, 6], 7))
print(Solution().searchInsert2([1, 3, 5, 6], 0))

# 解题思路: 二分法查询 时间复杂度O(log n)
