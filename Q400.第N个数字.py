#!/usr/bin/env python3

# https://leetcode-cn.com/problems/nth-digit
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
#
# 注意:
# n 是正数且在32为整形范围内 ( n < 2^31)。
#
# 示例 1:
# 输入:
# 3
# 输出:
# 3
#
# 示例 2:
# 输入:
# 11
# 输出:
# 0
#
# 说明:
# 第11个数字在序列 1234567891011, ... 里是0，它是10的一部分。
# 1  0  1  1  1  2  1  3  1  4  1  5  1  6
# 10 11 12 13 14 15 16 17 18 19 20 21 22 23


class Solution:
    def findNthDigit(self, n: int) -> int:
        k = 0
        count = 0

        while count < n:
            k += 1
            count += 9 * 10**(k - 1) * k
        clip_num = n - count + 9 * 10**(k - 1) * k

        k_num = (clip_num - 1) / k
        k_end = (clip_num - 1) % k
        num = 10**(k - 1) + k_num

        return int(str(num)[k_end])


print(Solution().findNthDigit(3))  # 3
print(Solution().findNthDigit(11))  # 0
print(Solution().findNthDigit(99))
