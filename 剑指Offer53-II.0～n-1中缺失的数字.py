# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，
# 并且每个数字都在范围0～n-1之内。
# 在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
#  
# 示例 1:
# 输入: [0,1,3]
# 输出: 2
#  
# 示例 2:
# 输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8
#  
# 限制：
# 1 <= 数组长度 <= 10000


class Solution:
    def missingNumber(self, nums: list) -> int:
        head, foot = 0, len(nums)
        while head < foot:
            middle = head + (foot - head) // 2
            if nums[middle] == middle:
                head = middle + 1
            else:
                foot = middle
        return head, foot

print(Solution().missingNumber([0,1,3]))    # 2
print(Solution().missingNumber([0,1,2,3,4,5,6,7,9]))    # 8
print(Solution().missingNumber([0]))    # 1
print(Solution().missingNumber([0,1]))  # 2