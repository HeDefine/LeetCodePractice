#!/usr/bin/env python3

# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
# 说明：
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
#
# 示例 1:
# 输入:
# s: "cbaebabacd" p: "abc"
# 输出:
# [0, 6]
#
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#
# 示例 2:
# 输入:
# s: "abab" p: "ab"
# 输出:
# [0, 1, 2]
#
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。


class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        result = list()
        pDict = dict()
        for ch in p:
            if pDict.get(ch) is None:
                pDict[ch] = 1
            else:
                pDict[ch] = pDict[ch] + 1
        i = 0

        while i <= len(s) - len(p):
            j = 0
            temp = pDict.copy()
            while j < len(p):
                ch = s[i + j]
                print(ch, temp)
                if temp.get(ch) is None:
                    break
                elif temp[ch] <= 0:
                    break
                else:
                    temp[ch] -= 1
                    if temp[ch] == 0:
                        del temp[ch]
                j += 1
            if len(temp) == 0:
                result.append(i)
            i += 1
        return result

    def findAnagrams2(self, s: str, p: str) -> [int]:
        result = []
        pDict = {}
        for ch in p:
            pDict[ch] = pDict.get(ch, 0) + 1

        sDict = {}
        for idx, ch in enumerate(s):
            sDict[ch] = sDict.get(ch, 0) + 1
            if sDict == pDict:
                result.append(idx - len(p) + 1)
            if idx - len(p) + 1 >= 0:
                c = s[idx - len(p) + 1]
                sDict[c] = sDict.get(c, 0) - 1
                if sDict[c] <= 0:
                    del sDict[c]

        return result

print(Solution().findAnagrams2("cbaebabacd", "abc"))  # [0,6]
# print(Solution().findAnagrams2("abab", "ab"))  # [0,1,2]

