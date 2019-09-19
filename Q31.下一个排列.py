#!/usr/bin/env python3

# https://leetcode-cn.com/problems/next-permutation
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        change = -1
        for idx, n in enumerate(nums):
            if idx > 0 and n > nums[idx - 1]:
                change = idx
        if change == -1:
            nums.reverse()
        else:
            for idx, n in enumerate(nums[change + 1:]):
                print(n)


print(Solution().nextPermutation([1, 2, 3, 4]))  # [1,3,2]
print(Solution().nextPermutation([3, 2, 1]))  # [1,2,3]
print(Solution().nextPermutation([1, 1, 5]))  # [1,5,1]
print(Solution().nextPermutation([2, 1, 4, 3]))  # [2,1,3]
