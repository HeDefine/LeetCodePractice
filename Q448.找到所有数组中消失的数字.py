#!/usr/bin/env python3

# https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
#
# 示例:
# 输入:
# [4,3,2,7,8,2,3,1]
# 输出:
# [5,6]


class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        for i in nums:
            if nums[abs(i)-1] > 0:
                nums[abs(i)-1] *= -1

        result = list()
        for idx, n in enumerate(nums):
            if n > 0:
                result.append(idx + 1)
        return result

print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # [5,6]
