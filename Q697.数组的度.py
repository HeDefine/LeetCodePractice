#!/usr/bin/env python3

# https://leetcode-cn.com/problems/degree-of-an-array
# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
# 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
#
# 示例 1:
# 输入: [1, 2, 2, 3, 1]
# 输出: 2
#
# 解释:
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
#
# 示例 2:
# 输入: [1,2,2,3,1,4,2]
# 输出: 6
#
# 注意:
# 1. nums.length 在1到50,000区间范围内。
# 2. nums[i] 是一个在0到49,999范围内的整数。


class Solution:
    def findShortestSubArray(self, nums: [int]) -> int:
        dic = dict()
        for idx, v in enumerate(nums):
            if dic.get(v) is None:
                dic[v] = [idx]
            else:
                dic[v].append(idx)
        maxL = 0
        res = 0
        for k, v in dic.items():
            if maxL < len(v):
                maxL = len(v)
                res = v[-1] - v[0] + 1
            elif maxL == len(v):
                res = min(res, v[-1] - v[0] + 1)
        return res


print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))  # 2
print(Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))  # 6
