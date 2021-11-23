# 给你一个下标从 0 开始的整数数组 nums ，
# 如果 恰好 删除 一个 元素后，数组 严格递增 ，那么请你返回 true ，否则返回 false 。
# 如果数组本身已经是严格递增的，请你也返回 true 。
# 数组 nums 是 严格递增 的定义为：对于任意下标的 1 <= i < nums.length 都满足 nums[i - 1] < nums[i] 。
#  
# 示例 1：
# 输入：nums = [1,2,10,5,7]
# 输出：true
# 解释：从 nums 中删除下标 2 处的 10 ，得到 [1,2,5,7] 。
# [1,2,5,7] 是严格递增的，所以返回 true 。
#  
# 示例 2：
# 输入：nums = [2,3,1,2]
# 输出：false
# 解释：
# [3,1,2] 是删除下标 0 处元素后得到的结果。
# [2,1,2] 是删除下标 1 处元素后得到的结果。
# [2,3,2] 是删除下标 2 处元素后得到的结果。
# [2,3,1] 是删除下标 3 处元素后得到的结果。
# 没有任何结果数组是严格递增的，所以返回 false 。
#  
# 示例 3：
# 输入：nums = [1,1,1]
# 输出：false
# 解释：删除任意元素后的结果都是 [1,1] 。
# [1,1] 不是严格递增的，所以返回 false 。
#  
# 示例 4：
# 输入：nums = [1,2,3]
# 输出：true
# 解释：[1,2,3] 已经是严格递增的，所以返回 true 。
#  
# 提示：
# 2 <= nums.length <= 1000
# 1 <= nums[i] <= 1000

class Solution:
    def canBeIncreasing(self, nums: list) -> bool:
        last_val = -1
        temp = 0
        idx = 0
        for idx, num in enumerate(nums):
            if idx + 1 < len(nums) and num >= nums[idx + 1]:
                if idx == 0 or (idx > 0 and nums[idx - 1] < nums[idx + 1]):
                    temp += 1
                    continue
                print(num)
            if last_val != -1 and last_val >= num:
                temp += 1
                print(num)
                continue
            last_val = num
        return temp <= 1
    
print(Solution().canBeIncreasing(nums = [1,2,10,5,7]))      # True
print(Solution().canBeIncreasing(nums = [2,3,1,2]))     # False
print(Solution().canBeIncreasing(nums = [1,1,1]))   # False
print(Solution().canBeIncreasing(nums = [1,2,3]))   # True
print(Solution().canBeIncreasing([1,2,10,5,7]))
print(Solution().canBeIncreasing([100,21,100]))
print(Solution().canBeIncreasing([36,604,874,425,249]))