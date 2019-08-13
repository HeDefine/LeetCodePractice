#!/usr/bin/env python3

# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 你找到的子数组应是最短的，请输出它的长度。
#
# 示例 1:
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#
# 说明 :
# 1.输入的数组长度范围在 [1, 10,000]。
# 2.输入的数组可能包含重复元素 ，所以升序的意思是<=


class Solution:
    def findUnsortedSubarray(self, nums: [int]) -> int:
        idx0 = 0
        idx1 = len(nums) - 1
        temp = sorted(nums)
        while idx0 < idx1:
            if temp[idx0] != nums[idx0] and temp[idx1] != nums[idx1]:
                return idx1 - idx0 + 1
            if temp[idx0] == nums[idx0]:
                idx0 += 1
            if temp[idx1] == nums[idx1]:
                idx1 -= 1
        return 0


print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))  # 5
print(Solution().findUnsortedSubarray([1, 2]))  # 0
print(Solution().findUnsortedSubarray([1, 3, 2, 2, 2]))
