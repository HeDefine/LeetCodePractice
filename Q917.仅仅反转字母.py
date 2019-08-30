#!/usr/bin/env python3

# https://leetcode-cn.com/problems/reverse-only-letters
# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
#
# 示例 1：
# 输入："ab-cd"
# 输出："dc-ba"
#
# 示例 2：
# 输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#
# 示例 3：
# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#
# 提示：
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S 中不包含 \ or "


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        head = 0
        last = len(S) - 1
        lS = list(S)
        while head < last:
            if ('a' <= lS[head] <= 'z' or 'A' <= lS[head] <= 'Z') and (
                    'a' <= lS[last] <= 'z' or 'A' <= lS[last] <= 'Z'):
                lS[head], lS[last] = lS[last], lS[head]
                head += 1
                last -= 1
            else:
                if not ('a' <= lS[head] <= 'z' or 'A' <= lS[head] <= 'Z'):
                    head += 1
                if not ('a' <= lS[last] <= 'z' or 'A' <= lS[last] <= 'Z'):
                    last -= 1
        return ''.join(lS)


print(Solution().reverseOnlyLetters("ab-cd"))  # dc-ba
print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))  # "j-Ih-gfE-dCba"
print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # "Qedo1ct-eeLg=ntse-T!"
