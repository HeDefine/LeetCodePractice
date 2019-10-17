#!/usr/bin/env python3

# https://leetcode-cn.com/problems/powx-n
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
# 示例 1:
# 输入: 2.00000, 10
# 输出: 1024.00000
#
# 示例 2:
# 输入: 2.10000, 3
# 输出: 9.26100
#
# 示例 3:
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
#
# 说明:
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。


class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        signal = n >= 0
        n = abs(n)
        while n != 0:
            if n % 2 == 1:
                res = res * x
            x = x * x
            n = n // 2
        return res if signal else 1 / res


print(Solution().myPow(2.0, 10))  # 1024
print(Solution().myPow(2.1, 3))  # 9.261
print(Solution().myPow(2.0, -2))  # 0.25
