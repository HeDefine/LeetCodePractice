#!/usr/bin/env python3

# https://leetcode-cn.com/problems/additive-number
# 累加数是一个字符串，组成它的数字可以形成累加序列。
# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
#
# 示例 1:
# 输入: "112358"
# 输出: true
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
#
# 示例 2:
# 输入: "199100199"
# 输出: true
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
#
# 进阶:
# 你如何处理一个溢出的过大的整数输入?


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def isAddNum(num1: str, num2: str, other: str) -> bool:
            if len(str(int(num1))) != len(num1) or len(str(int(num2))) != len(num2):
                return False
            sumV = str(int(num1) + int(num2))
            if sumV == other:
                return True
            if other.startswith(sumV):
                return isAddNum(num2, sumV, other[len(sumV):])
            else:
                return False

        for i in range(len(num) // 2):
            n1 = num[:i + 1]
            for j in range(i + 1, len(num) - 1):
                n2 = num[i + 1:j + 1]
                rest = num[j + 1:]
                if len(n1) > len(rest) or len(n2) > len(rest):
                    break
                if isAddNum(n1, n2, rest):
                    return True
        return False


print(Solution().isAdditiveNumber("112358"))  # True
print(Solution().isAdditiveNumber("199100199"))  # True
