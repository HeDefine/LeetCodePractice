#!/usr/bin/env python3

# https://leetcode-cn.com/problems/range-sum-query-immutable
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
#
# 示例：
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#
# 说明:
# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。


class NumArray:
    def __init__(self, nums: [int]):
        self.nums = nums
        self.sums = [0]
        for num in nums:
            self.sums.append(num + self.sums[-1])

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]


obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))  # 1
print(obj.sumRange(2, 5))  # -1
print(obj.sumRange(0, 5))  # -3
