#!/usr/bin/env python3

# https://leetcode-cn.com/problems/binary-number-with-alternating-bits
# 给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。
#
# 示例 1:
# 输入: 5
# 输出: True
# 解释:
# 5的二进制数是: 101
#
# 示例 2:
# 输入: 7
# 输出: False
# 解释:
# 7的二进制数是: 111
#
# 示例 3:
# 输入: 11
# 输出: False
# 解释:
# 11的二进制数是: 1011
#
#  示例 4:
# 输入: 10
# 输出: True
# 解释:
# 10的二进制数是: 1010
import math

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return math.log2(abs(~(n >> 1 ^ n))) == round(math.log2(abs(~(n >> 1 ^ n))))


print(Solution().hasAlternatingBits(4))  # False
print(Solution().hasAlternatingBits(5))  # True
print(Solution().hasAlternatingBits(7))  # False
print(Solution().hasAlternatingBits(11))  # False
print(Solution().hasAlternatingBits(10))  # True
