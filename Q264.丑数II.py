#!/usr/bin/env python3

# https://leetcode-cn.com/problems/ugly-number-ii
# 编写一个程序，找出第 n 个丑数。
# 丑数就是只包含质因数 2, 3, 5 的正整数。
#
# 示例:
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#
# 说明:  
# 1 是丑数。
# n 不超过1690。


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        temp = [1]
        heapq.heapify(temp)
        res = 0
        for _ in range(n):
            res = heapq.heappop(temp)
            while len(temp) > 0 and res == temp[0]:
                res = heapq.heappop(temp)
            heapq.heappush(temp, res * 2)
            heapq.heappush(temp, res * 3)
            heapq.heappush(temp, res * 5)
        return res



print(Solution().nthUglyNumber(10))  # 12
