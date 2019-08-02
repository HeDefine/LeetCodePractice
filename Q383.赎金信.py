#!/usr/bin/env python3

# https://leetcode-cn.com/problems/ransom-note
# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。
# 如果可以构成，返回 true ；否则返回 false。
#
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
#
# 注意：
#
# 你可以假设两个字符串均只含有小写字母。
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        dic0 = dict()
        dic1 = dict()
        for idx, n in enumerate(magazine):
            if dic0.get(n) is None:
                dic0[n] = 1
            else:
                dic0[n] = dic0[n] + 1
            if idx < len(ransomNote):
                v = ransomNote[idx]
                if dic1.get(v) is None:
                    dic1[v] = 1
                else:
                    dic1[v] = dic1[v] + 1
        for k, v in dic1.items():
            if dic0.get(k) is None or dic0.get(k) < v:
                return False
        return True


print(Solution().canConstruct("a", "b"))  # False
print(Solution().canConstruct("aa", "ab"))  # False
print(Solution().canConstruct("aa", "aab"))  # True
print(Solution().canConstruct("", ""))  # True
print(Solution().canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))  # True
