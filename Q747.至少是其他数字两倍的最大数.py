#!/usr/bin/env python3

# https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others
# 在一个给定的数组nums中，总是存在一个最大元素 。
# 查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
# 如果是，则返回最大元素的索引，否则返回-1。
#
# 示例 1:
# 输入: nums = [3, 6, 1, 0]
# 输出: 1
# 解释: 6是最大的整数, 对于数组中的其他整数,
# 6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
#
# 示例 2:
# 输入: nums = [1, 2, 3, 4]
# 输出: -1
# 解释: 4没有超过3的两倍大, 所以我们返回 -1.
#
# 提示:
# 1. nums 的长度范围在[1, 50].
# 2. 每个 nums[i] 的整数范围在 [0, 99].


class Solution:
    def dominantIndex(self, nums: [int]) -> int:
        res = 0
        temp = [0, 0]
        for idx, n in enumerate(nums):
            temp.append(n)
            if temp[0] < temp[-1]:
                temp[0], temp[-1] = temp[-1], temp[0]
                res = idx
            if temp[1] < temp[-1]:
                temp[1], temp[-1] = temp[-1], temp[1]
        if temp[0] >= temp[1] * 2:
            return res
        return -1


print(Solution().dominantIndex([3, 6, 1, 0]))  # 1
print(Solution().dominantIndex([1, 2, 3, 4]))  # -1
