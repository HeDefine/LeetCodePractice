#!/usr/bin/env python3

# https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
# 说明:
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
#
# 示例:
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。


class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        dic = dict()
        for idx, num in enumerate(numbers):
            if dic.get(target - num) is not None:
                return [idx, dic.get(target - num)]
            dic[num] = idx


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([-1, 1], 0))


# 题解，放到字典里。字典的查找的时间复杂度是O(1) 所以这个时间复杂度是O(n)
# 方法二也很容易想到. 利用双指针。
