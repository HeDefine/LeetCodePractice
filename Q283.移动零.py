#!/usr/bin/env python3

# https://leetcode-cn.com/problems/move-zeroes
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
# 说明:
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。


class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        idx = 0
        nums.append("end")
        while idx < len(nums):
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
            elif nums[idx] == "end":
                nums.pop(idx)
                break
            else:
                idx += 1


print(Solution().moveZeroes([0, 1, 0, 3, 12]))  # [1,3,12,0,0]
