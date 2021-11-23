# 一个 平方和三元组 (a,b,c) 指的是满足 a2 + b2 = c2 的 整数 三元组 a，b 和 c 。
# 给你一个整数 n ，请你返回满足 1 <= a, b, c <= n 的 平方和三元组 的数目。
#  
# 示例 1：
# 输入：n = 5
# 输出：2
# 解释：平方和三元组为 (3,4,5) 和 (4,3,5) 。
#  
# 示例 2：
# 输入：n = 10
# 输出：4
# 解释：平方和三元组为 (3,4,5)，(4,3,5)，(6,8,10) 和 (8,6,10) 。
#  
# 提示：
# 1 <= n <= 250

from math import sqrt
class Solution:
    def countTriples(self, n: int) -> int:
        res_dict = dict()
        for i in range(1, n+1):
            res_dict[i] = 1
        
        res = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if res_dict.get(sqrt(i**2 + j**2)) is not None:
                    res += 1
        return res
    
print(Solution().countTriples(5))   # 2
print(Solution().countTriples(10))  # 4