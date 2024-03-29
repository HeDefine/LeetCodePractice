#!/usr/bin/env python3

# https://leetcode-cn.com/problems/max-consecutive-ones
# 给定一个二进制数组， 计算其中最大连续1的个数。
#
# 示例 1:
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
#
# 注意：
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。


class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        result = 0
        temp = 0
        for num in nums:
            if num == 0:
                temp = 0
            else:
                temp += 1
                result = max(result, temp)
        return result


# print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # 3

print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
