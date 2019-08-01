#!/usr/bin/env python3

# https://leetcode-cn.com/problems/power-of-four
#
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
#
# 示例 1:
# 输入: 16
# 输出: true
#
# 示例 2:
# 输入: 5
# 输出: false


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 0:
            return False
        if num & (num - 1):
            return False
        return num & 0x55555555 != 0
        # return num % 3 == 1


print(Solution().isPowerOfFour(16))  # True
print(Solution().isPowerOfFour(5))  # False
print(Solution().isPowerOfFour(7))  # False
