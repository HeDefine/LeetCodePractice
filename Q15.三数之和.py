#!/usr/bin/env python3

# https://leetcode-cn.com/problems/3sum
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        res = list()
        nums.sort()
        for idx1, a in enumerate(nums):
            if idx1 > 0 and a == nums[idx1 - 1]:
                continue
            if idx1 < len(nums) - 2 and a <= 0:
                idx2 = idx1 + 1
                idx3 = len(nums) - 1
                while idx2 < idx3:
                    b = nums[idx2]
                    c = nums[idx3]
                    if a + b + c == 0:
                        res.append([a, b, c])
                        while idx2 + 1 < len(nums) and b == nums[idx2 + 1]:
                            idx2 += 1
                        while idx3 > idx1 and c == nums[idx3 - 1]:
                            idx3 -= 1
                        idx2 += 1
                        idx3 -= 1
                    elif a + b + c < 0:
                        idx2 += 1
                    else:
                        idx3 -= 1
        return res


# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([0, 0, 0]))
