#!/usr/bin/env python3

# https://leetcode-cn.com/problems/count-primes/
# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。


class Solution:
    def countPrimes(self, n: int) -> int:
        def isPrimeNum(v: int) -> bool:
            if v == 2:
                return True

            if v < 2:
                return False

            for j in range(2, v):
                if v % j == 0:
                    return False
            return True

        if n <= 1:
            return 0
        count = 0
        for i in range(2, n):
            if isPrimeNum(i):
                count += 1
        return count

    def countPrimes2(self, n: int) -> int:
        result = [True] * n
        count = 0
        for i in range(2, n):
            if result[i]:
                count += 1
                for j in range(2, n):
                    if i * j < n:
                        result[i * j] = False
                    else:
                        break
        return count


print(Solution().countPrimes2(2))

# 题解：暴力法, 最容易想到的办法，但是超时了
#   2. 厄拉多塞筛法
#   先将 2－N 的各数放入表中，然后在 2 的上面画一个圆圈，然后划去 2 的其他倍数；
#   第一个既未画圈又没有被划去的数是 3，将它画圈，再划去 3 的其他倍数；
#   现在既未画圈又没有被划去的第一个数是 5，将它画圈，并划去5的其他倍数……
#   依次类推，一直到所有小于或等于N的各数都画了圈或划去为止。
# 这时，表中画了圈的以及未划去的那些数正好就是小于 N 的素数。
