#!/usr/bin/env python3

# https://leetcode-cn.com/problems/height-checker
# 学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。
# 请你返回至少有多少个学生没有站在正确位置数量。该人数指的是：能让所有学生以 非递减 高度排列的必要移动人数。
#
# 示例：
# 输入：[1,1,4,2,1,3]
# 输出：3
# 解释：
# 高度为 4、3 和最后一个 1 的学生，没有站在正确的位置。
#
# 提示：
# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100


class Solution:
    def heightChecker(self, heights: [int]) -> int:
        sortHeights = sorted(heights)
        res = 0
        for idx, val in enumerate(heights):
            if val != sortHeights[idx]:
                res += 1
        return res


print(Solution().heightChecker([1, 1, 4, 2, 1, 3]))  # 3
