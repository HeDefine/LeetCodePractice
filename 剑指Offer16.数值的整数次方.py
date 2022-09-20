# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。
# 不得使用库函数，同时不需要考虑大数问题。
#  
# 示例 1：
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
#  
# 示例 2：
# 输入：x = 2.10000, n = 3
# 输出：9.26100
#  
# 示例 3：
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25
#  
# 提示：
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# -104 <= xn <= 104

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        t1 = self.myPow(x, n // 2)
        t2 = self.myPow(x, n % 2)
        return  t1 * t1 * t2
    
print(Solution().myPow(2, 10))  # 1024
print(Solution().myPow(2.1, 3)) # 9.261
print(Solution().myPow(2, -2))   # 0.25
print(Solution().myPow(0.00001,2147483647))