#!/usr/bin/env python3

# https://leetcode-cn.com/problems/valid-parentheses
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。


class Solution:
    def isValid(self, s: str) -> bool:
        l0 = list()
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                l0.append(ch)
            if ch == ")" or ch == "]" or ch == "}":
                if len(l0) == 0:
                    return False
                if ch == ")" and l0[len(l0) - 1] == "(":
                    l0.pop()
                elif ch == "]" and l0[len(l0) - 1] == "[":
                    l0.pop()
                elif ch == "}" and l0[len(l0) - 1] == "{":
                    l0.pop()
                else:
                    return False
        return len(l0) == 0


print(Solution().isValid("()"))  # True
print(Solution().isValid("()[]{}"))  # True
print(Solution().isValid("(]"))  # False
print(Solution().isValid("([)]"))  # False
print(Solution().isValid("{[]}"))  # True
print(Solution().isValid("]"))  # False
print(Solution().isValid("{]}"))  # False

# 解题思路: 利用先进后出的思路, 如果是"(" "[" "]"就推入，如果是")" "]" "}"就推出
# 推出之前判断最后一个是不是它对应的那个括号，如果不是，返回错误
