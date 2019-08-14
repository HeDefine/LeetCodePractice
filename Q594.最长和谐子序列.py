#!/usr/bin/env python3

# https://leetcode-cn.com/problems/longest-harmonious-subsequence
# 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
# 现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
#
# 示例 1:
# 输入: [1,3,2,2,5,2,3,7]
# 输出: 5
# 原因: 最长的和谐数组是：[3,2,2,2,3].
# 说明: 输入的数组长度最大不超过20,000.


class Solution:
    def findLHS(self, nums: [int]) -> int:
        dic = dict()
        res = 0
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
            if dic.get(n - 1) is not None:
                res = max(res, dic[n] + dic[n - 1])
            if dic.get(n + 1) is not None:
                res = max(res, dic[n] + dic[n + 1])
        return res


print(Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]))  # 5
