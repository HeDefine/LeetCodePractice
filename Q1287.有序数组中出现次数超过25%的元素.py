# 给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。
# 请你找到并返回这个整数
#  
# 示例：
# 输入：arr = [1,2,2,6,6,6,6,7,10]
# 输出：6
#  
# 提示：
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5

class Solution:
    def findSpecialInteger(self, arr: list) -> int:
        for idx, val in enumerate(arr):
            maxIdx = idx + (len(arr) // 4 if len(arr) > 3 else 1)
            if maxIdx < len(arr):
                if val == arr[maxIdx]:
                    return val
        return ''
        
print(Solution().findSpecialInteger([1,2,2,6,6,6,6,7,10]))
print(Solution().findSpecialInteger([1,2,2,10]))