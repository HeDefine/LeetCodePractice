#!/usr/bin/env python3

# https://leetcode-cn.com/problems/first-unique-character-in-a-string
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
# 案例:
# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.
#
# 注意事项：您可以假定该字符串只包含小写字母。


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = dict()
        for idx, ch in enumerate(s):
            if dic.get(ch) is not None:
                dic[ch].append(idx)
            else:
                dic[ch] = [idx]

        for k, v in dic.items():
            if len(v) == 1:
                return v[0]
        return -1


print(Solution().firstUniqChar("leetcode"))  # 0
print(Solution().firstUniqChar("loveleetcode"))  # 2
print(Solution().firstUniqChar("aadadaad"))  # -1
