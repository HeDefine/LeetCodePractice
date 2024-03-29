#!/usr/bin/env python3

# https://leetcode-cn.com/problems/product-of-array-except-self
# 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
# 示例:
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）


class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        leftList = [1]
        res = [0] * len(nums)
        for idx in range(len(nums) - 1):
            leftList.append(nums[idx] * leftList[-1])
        rightV = 1
        for idx in range(len(nums) - 1, -1, -1):
            res[idx] = rightV * leftList[idx]
            rightV = nums[idx] * rightV

        return res

print(Solution().productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]
