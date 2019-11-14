#!/usr/bin/env python3

# https://leetcode-cn.com/problems/contains-duplicate-iii
# 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。
#
# 示例 1:
# 输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true
#
# 示例 2:
# 输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true
#
# 示例 3:
# 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        if len(nums) == 0 or k == 0:
            return False
        for i in range(len(nums)):
            for j in range(i + 1, min(len(nums), i + k + 1)):
                val1, val2 = nums[i], nums[j]
                if abs(val1 - val2) <= t:
                    return True
        return False


print(Solution().containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0))  # True
print(Solution().containsNearbyAlmostDuplicate(nums=[1, 0, 1, 1], k=1, t=2))  # True
print(Solution().containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))  # False
print(Solution().containsNearbyAlmostDuplicate([2, 2], 3, 0))
print(Solution().containsNearbyAlmostDuplicate([7, 1, 3], 2, 3))
print(Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
