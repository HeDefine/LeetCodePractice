#!/usr/bin/env python3

# https://leetcode-cn.com/problems/maximum-product-subarray
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
#
# 示例 1:
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
# 示例 2:
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。


class Solution:
    def maxProduct(self, nums: [int]) -> int:
        resMin = nums[0]
        resMax = nums[0]
        minValue = nums[0]
        maxValue = nums[0]

        for num in nums[1:]:
            minV = minValue
            maxV = maxValue
            minValue = min(minV * num, maxV * num, num)
            maxValue = max(minV * num, maxV * num, num)
            resMin = min(resMin, minValue)
            resMax = max(resMax, maxValue)
        return resMax


print(Solution().maxProduct([2, 3, -2, 4]))  # 6
print(Solution().maxProduct([-2, 0, -1]))
