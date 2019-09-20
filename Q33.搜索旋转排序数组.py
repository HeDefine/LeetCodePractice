#!/usr/bin/env python3

# https://leetcode-cn.com/problems/search-in-rotated-sorted-array
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 你可以假设数组中不存在重复的元素。
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
# 示例 2:
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1


class Solution:
    def search(self, nums: [int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        res = -1
        while first <= last:
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
                    return -1
                print(nums[first], nums[mid], nums[last])
        return res


print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))  # 4
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))  # -1
print(Solution().search([1], 1))
print(Solution().search([1, 3], 2))
print(Solution().search([1, 3, 5], 2))
print(Solution().search([8, 9, 2, 3, 4], 9))
print(Solution().search([5, 1, 3], 6))
