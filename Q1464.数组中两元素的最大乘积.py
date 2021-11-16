# 给你一个整数数组 nums，请你选择数组的两个不同下标 i 和 j，使 (nums[i]-1)*(nums[j]-1) 取得最大值。
# 请你计算并返回该式的最大值。
#  
# 示例 1：
# 输入：nums = [3,4,5,2]
# 输出：12 
# 解释：如果选择下标 i=1 和 j=2（下标从 0 开始），则可以获得最大值，(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12 。 
#  
# 示例 2：
# 输入：nums = [1,5,4,5]
# 输出：16
# 解释：选择下标 i=1 和 j=3（下标从 0 开始），则可以获得最大值 (5-1)*(5-1) = 16 。
#  
# 示例 3：
# 输入：nums = [3,7]
# 输出：12
#  
# 提示：
# 2 <= nums.length <= 500
# 1 <= nums[i] <= 10^3

class Solution:
    def maxProduct(self, nums: list) -> int:
        max_num, max_next_num = max(nums[0], nums[1]), min(nums[0], nums[1])
        for idx in range(2, len(nums)):
            num = nums[idx]
            if num >= max_num >= max_next_num:
                max_num, max_next_num = num, max_num
            elif max_num >= num >= max_next_num:
                max_next_num = num
        return (max_num - 1) * (max_next_num - 1)
                
    
print(Solution().maxProduct(nums = [3,4,5,2]))  # 12
print(Solution().maxProduct(nums = [1,5,4,5]))  # 16
print(Solution().maxProduct(nums = [3,7]))  # 12
print(Solution().maxProduct([10,2,5,2]))    # 36