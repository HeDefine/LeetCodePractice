#!/usr/bin/env python3

# https://leetcode-cn.com/problems/4sum
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 注意：
# 答案中不可以包含重复的四元组。
#
# 示例：
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        res = list()
        nums.sort()
        for idx1, a in enumerate(nums):
            if idx1 > 0 and a == nums[idx1 - 1]:
                continue
            if idx1 < len(nums) - 3:
                for idx2 in range(idx1 + 1, len(nums) - 2):
                    b = nums[idx2]
                    if idx2 > idx1 + 1 and b == nums[idx2 - 1]:
                        continue
                    if idx2 < len(nums) - 2:
                        idx3 = idx2 + 1
                        idx4 = len(nums) - 1
                        while idx3 < idx4:
                            c = nums[idx3]
                            d = nums[idx4]
                            if a + b + c + d == target:
                                res.append([a, b, c, d])
                                while idx3 + 1 < len(nums) and c == nums[idx3 + 1]:
                                    idx3 += 1

                                while idx4 > idx2 and d == nums[idx4 - 1]:
                                    idx4 -= 1
                                idx3 += 1
                                idx4 -= 1
                            elif a + b + c + d < target:
                                idx3 += 1
                            else:
                                idx4 -= 1
        return res


print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
print(Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
# [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

print(Solution().fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))
