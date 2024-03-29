#!/usr/bin/env python3

# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
#
# 示例 2:
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
#
# 说明：
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
#
# 进阶:
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？


class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        nums1.sort()
        nums2.sort()

        i1 = 0
        i2 = 0
        result = list()
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                result.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return result


print(Solution().intersect([1, 2, 2, 1], [2, 2]))  # [2,2]
print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4,9]
