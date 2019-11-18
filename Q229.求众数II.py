#!/usr/bin/env python3

# https://leetcode-cn.com/problems/majority-element-ii
# 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
#
# 示例 1:
# 输入: [3,2,3]
# 输出: [3]
#
# 示例 2:
# 输入: [1,1,1,3,3,2,2,2]
# 输出: [1,2]


class Solution:
    def majorityElement(self, nums: [int]) -> [int]:
        a, aNum, aCount = None, 0, 0
        b, bNum, bCount = None, 0, 0
        for val in nums:
            if a == val:
                aNum += 1
            elif b == val:
                bNum += 1
            elif aNum == 0:
                a, aNum = val, 1
            elif bNum == 0:
                b, bNum = val, 1
            else:
                aNum -= 1
                bNum -= 1

        for val in nums:
            if a == val:
                aCount += 1
            elif b == val:
                bCount += 1
        return ([a] if aCount > len(nums) // 3 else []) + ([b] if bCount > len(nums) // 3 else [])


print(Solution().majorityElement([3, 2, 3]))  # [3]
print(Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))  # [1,2]
