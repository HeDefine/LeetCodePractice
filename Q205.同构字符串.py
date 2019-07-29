#!/usr/bin/env python3

# https://leetcode-cn.com/problems/isomorphic-strings
# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
#
# 示例 1:
# 输入: s = "egg", t = "add"
# 输出: true
#
# 示例 2:
# 输入: s = "foo", t = "bar"
# 输出: false
#
# 示例 3:
# 输入: s = "paper", t = "title"
# 输出: true
# 说明:
# 你可以假设 s 和 t 具有相同的长度。


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sdic = dict()
        tdic = dict()
        for idx in range(len(s)):
            ch1 = s[idx]
            ch2 = t[idx]

            if sdic.get(ch1) is None:
                sdic[ch1] = [idx]
            else:
                sdic[ch1].append(idx)

            if tdic.get(ch2) is None:
                tdic[ch2] = [idx]
            else:
                tdic[ch2].append(idx)

            if sdic[ch1] != tdic[ch2]:
                return False

        return True


print(Solution().isIsomorphic("egg", "add"))  # True
print(Solution().isIsomorphic("foo", "bar"))  # False
print(Solution().isIsomorphic("paper", "title"))  # True
