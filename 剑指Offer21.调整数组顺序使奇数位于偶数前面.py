# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。
#  
# 示例：
# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4] 
# 注：[3,1,2,4] 也是正确的答案之一。
#  
# 提示：
# 0 <= nums.length <= 50000
# 0 <= nums[i] <= 10000

class Solution:
    def exchange(self, nums: list) -> list:
        left_idx, right_idx = 0, len(nums)-1
        while left_idx < right_idx:
            if nums[left_idx] % 2 == 0 and nums[right_idx] % 2 == 1:
                nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
                left_idx += 1
                right_idx -= 1
            
            if nums[left_idx] % 2 == 1:
                left_idx += 1
            if nums[right_idx] % 2 == 0:
                right_idx -= 1
            
                
            print(nums)
        return nums

# print(Solution().exchange([1,2,3,4]))   # [1,3,2,4] 
print(Solution().exchange([11,9,3,7,16,4,2,0]))
