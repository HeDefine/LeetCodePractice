#!/usr/bin/env python3

# https://leetcode-cn.com/problems/3sum-closest
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).


class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for idx1, a in enumerate(nums):
            if idx1 > 0 and nums[idx1 - 1] == a:
                continue
            if idx1 < len(nums) - 2:
                idx2 = idx1 + 1
                idx3 = len(nums) - 1

                while idx2 < idx3:
                    b = nums[idx2]
                    c = nums[idx3]
                    sumV = a + b + c
                    if sumV == target:
                        return target
                    elif sumV < target:
                        if abs(sumV - target) < abs(res - target):
                            res = sumV
                        idx2 += 1
                    else:
                        if abs(sumV - target) < abs(res - target):
                            res = sumV
                        idx3 -= 1
        return res


# print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
# print(Solution().threeSumClosest([0, 1, 2], 3))
# print(Solution().threeSumClosest([0, 1, 2], 0))
print(Solution().threeSumClosest(
    [6, -18, -20, -7, -15, 9, 18, 10, 1, -20, -17, -19, -3, -5, -19, 10, 6, -11, 1, -17, -15, 6, 17, -18, -3, 16, 19,
     -20, -3, -17, -15, -3, 12, 1, -9, 4, 1, 12, -2, 14, 4, -4, 19, -20, 6, 0, -19, 18, 14, 1, -15, -5, 14, 12, -4, 0,
     -10, 6, 6, -6, 20, -8, -6, 5, 0, 3, 10, 7, -2, 17, 20, 12, 19, -13, -1, 10, -1, 14, 0, 7, -3, 10, 14, 14, 11, 0,
     -4, -15, -8, 3, 2, -5, 9, 10, 16, -4, -3, -9, -8, -14, 10, 6, 2, -12, -7, -16, -6, 10]
    , -52))
