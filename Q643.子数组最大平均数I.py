#!/usr/bin/env python3

# https://leetcode-cn.com/problems/maximum-average-subarray-i
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
#
# 示例 1:
# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
#  
# 注意:
# 1 <= k <= n <= 30,000。
# 所给数据范围 [-10,000，10,000]。


class Solution:
    def findMaxAverage(self, nums: [int], k: int) -> float:
        maxV = None
        sumV = 0
        for idx, num in enumerate(nums):
            if idx + 1 - k == 0:
                sumV += num
                maxV = sumV
            elif idx + 1 - k > 0:
                sumV = sumV + num - nums[(idx - k)]
                maxV = max(maxV, sumV)
            else:
                sumV += num
        return maxV / k


print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # 12.75
print(Solution().findMaxAverage([-5], 1))  # -5
print(Solution().findMaxAverage([3, 3, 4, 3, 0], 3))
print(Solution().findMaxAverage(
    [-6662, 5432, -8558, -8935, 8731, -3083, 4115, 9931, -4006, -3284, -3024, 1714, -2825, -2374, -2750, -959, 6516,
     9356, 8040, -2169, -9490, -3068, 6299, 7823, -9767, 5751, -7897, 6680, -1293, -3486, -6785, 6337, -9158, -4183,
     6240, -2846, -2588, -5458, -9576, -1501, -908, -5477, 7596, -8863, -4088, 7922, 8231, -4928, 7636, -3994, -243,
     -1327, 8425, -3468, -4218, -364, 4257, 5690, 1035, 6217, 8880, 4127, -6299, -1831, 2854, -4498, -6983, -677, 2216,
     -1938, 3348, 4099, 3591, 9076, 942, 4571, -4200, 7271, -6920, -1886, 662, 7844, 3658, -6562, -2106, -296, -3280,
     8909, -8352, -9413, 3513, 1352, -8825], 90))
