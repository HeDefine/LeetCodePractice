#!/usr/bin/env python3

# https://leetcode-cn.com/problems/non-decreasing-array
#
# 给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。
#
# 示例 1:
# 输入: [4,2,3]
# 输出: True
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
#
# 示例 2:
# 输入: [4,2,1]
# 输出: False
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
# 说明:  n 的范围为 [1, 10,000]。


class Solution:
    def checkPossibility(self, nums: [int]) -> bool:
        count = 0
        for idx, n in enumerate(nums):
            if count > 1:
                return False
            if idx + 1 < len(nums) and n > nums[idx + 1]:
                purpose1 = n
                purpose2 = nums[idx + 1]
                if (idx - 1 >= 0 and nums[idx - 1] <= purpose1) and (
                        idx + 2 < len(nums) and purpose1 <= nums[idx + 2]):
                    count += 1
                elif (idx - 1 >= 0 and nums[idx - 1] <= purpose2) and (
                        idx + 2 < len(nums) and purpose2 <= nums[idx + 2]):
                    count += 1
                elif idx == 0 and idx + 2 < len(nums) and (purpose1 <= nums[idx + 2] or purpose2 <= nums[idx + 2]):
                    count += 1
                elif idx + 2 >= len(nums):
                    count += 1
                else:
                    return False
        return True


# print(Solution().checkPossibility([4, 2, 3]))  # True
# print(Solution().checkPossibility([4, 2, 1]))  # False
# print(Solution().checkPossibility([3, 4, 2, 3]))  # False
# print(Solution().checkPossibility([2, 3, 3, 2, 4]))  # True
print(Solution().checkPossibility([1, 3, 2]))  # True
