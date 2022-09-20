# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
# 其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积,
# 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。
# 不能使用除法。
#  
# 示例:
# 输入: [1,2,3,4,5]
# 输出: [120,60,40,30,24]
#  
# 提示：
# 所有元素乘积之和不会溢出 32 位整数
# a.length <= 100000

class Solution:
    def constructArr(self, a: list) -> list:
        res = [1] * len(a)
        for i in range(len(a) - 1, -1, -1):
            if i + 1 < len(a):
                res[i] *= a[i + 1]
            if i + 1 < len(res):
                res[i] *= res[i + 1]
        t = 1
        for idx, val in enumerate(a):
            res[idx] *= t
            t = t * val 
        return res
        
print(Solution().constructArr([1,2,3,4,5]))