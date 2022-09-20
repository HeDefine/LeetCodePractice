# 从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
#  
# 示例 1:
# 输入: [1,2,3,4,5]
# 输出: True
#  
# 示例 2:
# 输入: [0,0,1,2,5]
# 输出: True
#  
# 限制：
# 数组长度为 5 
# 数组的数取值为 [0, 13] .

class Solution:
    def isStraight(self, nums: list) -> bool:
        nums.sort()
        zero_count = 0
        for idx, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            elif idx + 1 < len(nums):
                t = nums[idx + 1] - num
                if t == 0:
                    return False
                if t > 1:
                    zero_count -= (t - 1)
        return zero_count >= 0

print(Solution().isStraight([1,2,3,4,5]))   # True
print(Solution().isStraight([0,0,1,2,5]))   # True
print(Solution().isStraight([5,0,1,2,0]))   # True