#!/usr/bin/env python3

# https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#
# 示例 1:
# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
#
# 示例 2:
# 输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
#
# 进阶:
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？


class Solution:
    def search(self, nums: [int], target: int) -> bool:
        first = 0
        last = len(nums) - 1
        res = -1
        while first <= last:
            if nums[first] == nums[last]:
                last -= 1
                continue
            mid = (first + last) // 2
            if nums[mid] == target:
                res = mid
                break
            elif target == nums[first]:
                res = first
                break
            elif target == nums[last]:
                res = last
                break
            else:
                if first == mid or last == mid:
                    break
                if nums[first] < target < nums[mid]:
                    last = mid - 1
                elif nums[first] < target and target > nums[mid]:
                    if nums[mid] < nums[first]:
                        last = mid - 1
                    else:
                        first = mid + 1
                elif nums[mid] < target < nums[last]:
                    first = mid + 1
                elif target < nums[last] and target < nums[mid]:
                    if nums[mid] > nums[last]:
                        first = mid + 1
                    else:
                        last = mid - 1
                elif nums[first] > target > nums[last]:
                    return False
        return False if res == -1 else True


print(Solution().search([2, 5, 6, 0, 0, 1, 2], 0))  # True
print(Solution().search([2, 5, 6, 0, 0, 1, 2], 3))  # False
print(Solution().search([1, 3, 1, 1, 1], 3))  # True
