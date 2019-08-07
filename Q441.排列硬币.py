#!/usr/bin/env python3

# https://leetcode-cn.com/problems/arranging-coins
# 你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
# 给定一个数字 n，找出可形成完整阶梯行的总行数。
# n 是一个非负整数，并且在32位有符号整型的范围内。
#
# 示例 1:
# n = 5
# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤
# 因为第三行不完整，所以返回2.
#
# 示例 2:
# n = 8
# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# 因为第四行不完整，所以返回3.


class Solution:
    def arrangeCoins(self, n: int) -> int:
        result = 0
        sumV = 0
        for i in range(n + 1):
            sumV += i
            if sumV > n:
                break
            result = i
        return result

    def arrangeCoins2(self, n: int) -> int:
        minV = 0
        maxV = n
        while minV <= maxV:
            mid = (minV + maxV) // 2
            sum0 = (1 + mid) * mid // 2
            sum1 = (1 + mid + 1) * (mid + 1) // 2
            if sum0 <= n < sum1:
                return mid
            elif sum0 < n:
                minV = mid + 1
            elif sum0 > n:
                maxV = mid - 1


# print(Solution().arrangeCoins2(5))  # 2
# print(Solution().arrangeCoins2(8))  # 3
print(Solution().arrangeCoins2(10))  # 3
# 等差数列求和   S = (s1 + sn) * n / 2
