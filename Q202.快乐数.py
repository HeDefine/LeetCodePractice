#!/usr/bin/env python3

# https://leetcode-cn.com/problems/happy-number
# 编写一个算法来判断一个数是不是“快乐数”。
#
# 一个“快乐数”定义为：
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
# 然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。
# 如果可以变为 1，那么这个数就是快乐数。
#
# 示例: 
# 输入: 19
# 输出: true
# 解释:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1


class Solution:
    def isHappy(self, n: int) -> bool:
        def checkNum(v: int, allResult: [int]):
            result = 0
            while v > 0:
                result += pow(v % 10, 2)
                v = v // 10
            if result == 1:
                return True
            if allResult.count(result) > 0:
                return False
            else:
                allResult.append(result)
                return checkNum(result, allResult)
        return checkNum(n, [0])

# print(Solution().isHappy(19))       # True
print(Solution().isHappy(7))  # False
print(Solution().isHappy(11))  # False
