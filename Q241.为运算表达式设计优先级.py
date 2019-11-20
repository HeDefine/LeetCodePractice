#!/usr/bin/env python3

# https://leetcode-cn.com/problems/different-ways-to-add-parentheses
# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
#
# 示例 1:
#
# 输入: "2-1-1"
# 输出: [0, 2]
# 解释:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# 示例 2:
#
# 输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
#


class Solution:
    def diffWaysToCompute(self, input: str) -> [int]:
        if input.isdigit():
            return [int(input)]
        res = []
        for idx, ch in enumerate(input):
            if ch == '+' or ch == '-' or ch == '*':
                left = self.diffWaysToCompute(input[:idx])
                right = self.diffWaysToCompute(input[idx + 1:])
                for lVal in left:
                    for rVal in right:
                        if ch == '+':
                            res.append(lVal + rVal)
                        elif ch == '-':
                            res.append(lVal - rVal)
                        else:
                            res.append(lVal * rVal)
        return res


print(Solution().diffWaysToCompute('2-1-1'))  # [0,2]
print(Solution().diffWaysToCompute('2*3-4*5'))  # [-34, -14, -10, -10, 10]
