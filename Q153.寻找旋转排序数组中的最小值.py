#!/usr/bin/env python3

# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 请找出其中最小的元素。
# 你可以假设数组中不存在重复元素。
#
# 示例 1:
# 输入: [3,4,5,1,2]
# 输出: 1
#
# 示例 2:
# 输入: [4,5,6,7,0,1,2]
# 输出: 0


class Solution:
    def findMin(self, nums: [int]) -> int:
        begin = 0
        end = len(nums) - 1
        res = nums[0]
        while begin < end:
            mid = (begin + end) // 2
            if nums[mid] < nums[begin]:
                end = mid
                res = min(res, nums[mid])
            elif nums[begin] < nums[mid]:
                begin = mid
                res = min(res, nums[begin])
            else:
                if begin == mid or end == mid:
                    return min(res, nums[begin], nums[end])
        return nums[begin]


# print(Solution().findMin([3, 4, 5, 1, 2]))  # 1
# print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
print(Solution().findMin([2, 1]))
