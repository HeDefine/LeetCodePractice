#!/usr/bin/env python3

# https://leetcode-cn.com/problems/largest-number
# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
#
# 示例 1:
# 输入: [10,2]
# 输出: 210
#
# 示例 2:
# 输入: [3,30,34,5,9]
# 输出: 9534330
#
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。


class Solution:
    def largestNumber(self, nums: [int]) -> str:
        res = ''
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        for num in nums:
            res += str(num)
        return str(int(res))


print(Solution().largestNumber([10, 2]))  # 210
print(Solution().largestNumber([3, 30, 34, 5, 9]))  # 9534330
print(Solution().largestNumber([0, 0]))
