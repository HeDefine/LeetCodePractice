#!/usr/bin/env python3

# https://leetcode-cn.com/problems/merge-sorted-array#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，
# 使得 num1 成为一个有序数组。
#
# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
# 示例:
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 输出: [1,2,2,3,5,6]


class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        minV = min(nums1[0], nums2[0])
        i = m - 1
        j = n - 1
        while i + j + 1 >= 0:
            v1 = nums1[i] if i >= 0 else minV
            v2 = nums2[j] if j >= 0 else minV
            if v1 >= v2:
                nums1[i + j + 1] = v1
                i -= 1
            else:
                nums1[i + j + 1] = v2
                j -= 1


# n1 = [1, 2, 3, 0, 0, 0]
# n2 = [2, 5, 6]
#
n1 = [2, 0]
n2 = [1]

# n1 = [1, 2, 3, 0, 0, 0]
# n2 = [4, 5, 6]

Solution().merge(n1, 1, n2, 1)
print(n1)


# 题解: 用双指针