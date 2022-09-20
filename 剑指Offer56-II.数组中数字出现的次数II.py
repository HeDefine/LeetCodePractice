# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。
# 请找出那个只出现一次的数字。
#  
# 示例 1：
# 输入：nums = [3,4,3,3]
# 输出：4
#  
# 示例 2：
# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1
#  
# 限制：
# 1 <= nums.length <= 10000
# 1 <= nums[i] < 2^31

class Solution:
    def singleNumber(self, nums: list) -> int:
        res = dict()
        for num in nums:
            res[num] = res.get(num, 0) + 1
            
        for key in res.keys():
            if res[key] == 1:
                return key
        return -1

print(Solution().singleNumber([3,4,3,3]))   # 4
print(Solution().singleNumber([9,1,7,9,7,9,7])) # 1