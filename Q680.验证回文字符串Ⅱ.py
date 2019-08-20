#!/usr/bin/env python3

# https://leetcode-cn.com/problems/valid-palindrome-ii
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#
# 示例 1:
# 输入: "aba"
# 输出: True
#
# 示例 2:
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
#
# 注意:
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkIsPalindrome(st: str) -> bool:
            idx0 = 0
            idx1 = len(st) - 1
            while idx0 < idx1:
                if st[idx0] == st[idx1]:
                    idx0 += 1
                    idx1 -= 1
                else:
                    return False
            return True

        startIdx = 0
        endIdx = len(s) - 1
        while startIdx < endIdx:
            if s[startIdx] == s[endIdx]:
                startIdx += 1
                endIdx -= 1
            else:
                return checkIsPalindrome(s[startIdx + 1: endIdx + 1]) or checkIsPalindrome(s[startIdx:endIdx])

        return True


print(Solution().validPalindrome("aba"))
print(Solution().validPalindrome("abca"))
print(Solution().validPalindrome(
    "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
