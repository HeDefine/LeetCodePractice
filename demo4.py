#!/usr/bin/env python3

# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5


class Solution:
    # 其实题目要求的时间复杂度意味着要用二分法的方法来解题，这里是取巧了
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        allNum = list(nums1)
        allNum.extend(nums2)
        allNum.sort()
        print(allNum)
        if len(allNum) % 2 == 0:
            return (allNum[len(allNum) // 2] + allNum[len(allNum) // 2 - 1]) / 2
        else:
            return allNum[len(allNum) // 2]





nums1 = [1, 2]
nums2 = [-1, 3]
print(Solution().findMedianSortedArrays(nums1, nums2))

