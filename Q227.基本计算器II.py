#!/usr/bin/env python3

# https://leetcode-cn.com/problems/basic-calculator-ii
# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
# 字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
#
# 示例 1:
# 输入: "3+2*2"
# 输出: 7
#
# 示例 2:
# 输入: " 3/2 "
# 输出: 1
#
# 示例 3:
# 输入: " 3+5 / 2 "
# 输出: 5
#
# 说明：
# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval。


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        numStr = s.replace('+', '_')
        numStr = numStr.replace('-', '_')
        numStr = numStr.replace('*', '_')
        numStr = numStr.replace('/', '_')

        numList = numStr.split('_')
        idx = 1
        for ch in s:
            if ch == '+' or ch == '-':
                numList[idx] = ch + numList[idx]
                idx += 1
            elif ch == '*' or ch == '/':
                print(idx, numList, ch)
                val1 = int(numList[idx - 1])
                val2 = int(numList.pop(idx))
                if ch == '*':
                    numList[idx - 1] = str(val1 * val2)
                else:
                    flag = val1 * val2 >= 0
                    numList[idx - 1] = ('' if flag else '-') + str(abs(val1 // val2))
        res = 0
        print(numList)
        for n in numList:
            res += int(n) if n != '' else 0
        return res


# print(Solution().calculate("3+2*2"))  # 7
# print(Solution().calculate("3/2"))  # 1
# print(Solution().calculate("3+5/2"))  # 5
# print(Solution().calculate("42"))
# print(Solution().calculate('-42+2'))
# print(Solution().calculate('+42+2'))
# print(Solution().calculate('42+2+3-3'))
# print(Solution().calculate(" 3/2 "))
print(Solution().calculate("14/3*2"))
print(Solution().calculate("14-3/2"))