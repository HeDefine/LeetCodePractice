#!/usr/bin/env python3

# https://leetcode-cn.com/problems/contains-duplicate-ii
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。
#
# 示例 1:
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
#
# 示例 2:
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
#
# 示例 3:
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false


class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        dic = dict()
        for idx, num in enumerate(nums):
            if dic.get(num) is None:
                dic[num] = [idx]
            else:
                if idx - dic[num][-1] <= k:
                    return True
                dic[num].append(idx)
        return False


print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))  # True
print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))  # True
print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # False
