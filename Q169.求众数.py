#!/usr/bin/env python3

# https://leetcode-cn.com/problems/majority-element
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
#
# 示例 1:
# 输入: [3,2,3]
# 输出: 3
#
# 示例 2:
# 输入: [2,2,1,1,1,2,2]
# 输出: 2


class Solution:
    def majorityElement(self, nums: [int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement2(self, nums: [int]) -> int:
        dic = dict()
        for num in nums:
            if dic.get(num) is None:
                dic[num] = 1
            else:
                dic[num] += 1
        k, v = max(zip(dic.values(), dic.keys()))
        return v


print(Solution().majorityElement2([3, 2, 3]))  # 3
print(Solution().majorityElement2([2, 2, 1, 1, 1, 2, 2]))  # 2


# 题解：  1. 排序法去中值:   排序算法的时间复杂度是 O(nlogn)
