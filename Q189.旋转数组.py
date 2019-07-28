#!/usr/bin/env python3

# https://leetcode-cn.com/problems/rotate-array
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
# 示例 2:
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
# 说明:
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。


class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        while k > 0:
            v = nums.pop(-1)
            nums.insert(0, v)
            k -= 1


    def rotate2(self, nums: [int], k: int) -> None:
        nums.reverse()
        while k > 0:
            v = nums.pop(0)
            nums.append(v)
            k -= 1
        nums.reverse()


num1 = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate2(num1, 3)
print(num1)
