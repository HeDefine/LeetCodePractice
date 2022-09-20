# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
# 示例 1：
# 输入：n = 2
# 输出：2
#
# 示例 2：
# 输入：n = 7
# 输出：21
#
# 示例 3：
# 输入：n = 0
# 输出：1
#
# 提示：
# 0 <= n <= 100

class Solution:
    def numWays(self, n: int) -> int:
        [1, 1, 2, 3, 5, 8, 13, 21]
        def recursion(n) -> list:
            if n == 0:
                return [1]
            elif n < 0:
                return [0]
            
            
        return self.numWays(n-1) + self.numWays(n-2)

# print(Solution().numWays(2))    # 2
# print(Solution().numWays(7))    # 21
# print(Solution().numWays(0))    # 1
print(Solution().numWays(36))