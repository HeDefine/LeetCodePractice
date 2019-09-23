#!/usr/bin/env python3

# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 你的算法时间复杂度必须是 O(log n) 级别。
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2:
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]


class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        res = [-1, -1]
        idx0 = 0
        idx1 = len(nums) - 1
        while idx0 <= idx1:
            mid = (idx0 + idx1) // 2
            if nums[mid] == target and (mid == 0 or (mid > 0 and nums[mid - 1] != target)):
                res[0] = mid
                break
            elif nums[mid] < target:
                idx0 = mid + 1
            else:
                idx1 = mid - 1

        idx0 = 0
        idx1 = len(nums) - 1
        while idx0 <= idx1:
            mid = (idx0 + idx1) // 2
            if nums[mid] == target and (mid == len(nums) - 1 or (mid + 1 < len(nums) and nums[mid + 1] != target)):
                res[1] = mid
                break
            elif nums[mid] > target:
                idx1 = mid - 1
            else:
                idx0 = mid + 1
        return res


print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))  # [3,4]
print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))  # [-1,-1]
