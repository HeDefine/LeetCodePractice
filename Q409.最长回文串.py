#!/usr/bin/env python3

# https://leetcode-cn.com/problems/longest-palindrome
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
#
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
#
# 注意:
# 假设字符串的长度不会超过 1010。
#
# 示例 1:
# 输入:
# "abccccdd"
# 输出:
# 7
#
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = dict()

        for ch in s:
            if dic.get(ch) is not None:
                del dic[ch]
            else:
                dic[ch] = "1"
        if len(dic) == 0:
            return len(s) - len(dic)
        else:
            return len(s) - len(dic) + 1



print(Solution().longestPalindrome("abccccdd"))  # 7
