
# 方法1: 牺牲空间来节省时间
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        temp = dict()
        for num in nums:
            if temp.get(num) is not None:
                return num;
            temp[num] = 1;
        return 0
        
# 方法2: 原地置换
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for idx, val in enumerate(nums):
            if idx != val:
                i = idx
                while 1:
                    if nums[i] == -1:
                        return i
                    i = nums[i]
                    nums[i] = -1
        return 0
        
