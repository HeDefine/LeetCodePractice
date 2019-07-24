#!/usr/bin/env python3

# https://leetcode-cn.com/problems/pascals-triangle-ii
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
# 输入: 3
# 输出: [1,3,3,1]
#
# 进阶：
# 你可以优化你的算法到 O(k) 空间复杂度吗？


class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        result = [1] * (rowIndex + 1)
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                result[j] = result[j] + result[j - 1]
        return result


print(Solution().getRow(2))  # [1,3,3,1]
