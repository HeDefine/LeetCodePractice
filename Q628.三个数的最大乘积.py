#!/usr/bin/env python3

# https://leetcode-cn.com/problems/maximum-product-of-three-numbers
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
#
# 示例 1:
# 输入: [1,2,3]
# 输出: 6
#
# 示例 2:
# 输入: [1,2,3,4]
# 输出: 24
#
# 注意:
# 给定的整型数组长度范围是[3,10^4]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。


class Solution:
    def maximumProduct(self, nums: [int]) -> int:
        nums.sort()
        # 结果是正数, 多个正数中三个最大的正数
        res1 = nums[-1] * nums[-2] * nums[-3]
        # 结果是正数, 多个负数中两个最小的负数, 多个正数中一个最大正数
        res2 = nums[0] * nums[1] * nums[-1]
        # 结果是负数，只有两个正数, 多个负数中一个最大负数
        res3 = nums[-1] * nums[-2] * nums[-3]
        # 结果是负数，全都是负数, 多个负数中最大的三个负数
        res4 = nums[-1] * nums[-2] * nums[-3]

        return max(res1, res2)




print(Solution().maximumProduct([1, 2, 3]))  # 6
print(Solution().maximumProduct([1, 2, 3, 4]))  # 24
