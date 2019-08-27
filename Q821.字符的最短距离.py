#!/usr/bin/env python3

# https://leetcode-cn.com/problems/shortest-distance-to-a-character
# 给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
#
# 示例 1:
# 输入: S = "loveleetcode", C = 'e'
# 输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#
# 说明:
# 字符串 S 的长度范围为 [1, 10000]。
# C 是一个单字符，且保证是字符串 S 里的字符。
# S 和 C 中的所有字母均为小写字母。


class Solution:
    def shortestToChar(self, S: str, C: str) -> [int]:
        res = list()
        minIdx = -1
        maxIdx = S.find(C)
        for idx, ch in enumerate(S):
            if idx < maxIdx != -1 and minIdx == -1:
                res.append(abs(idx - maxIdx))
            elif idx == maxIdx:
                res.append(0)
                minIdx = idx
                maxIdx = S.find(C, idx + 1)
            elif minIdx < idx < maxIdx:
                res.append(min(abs(minIdx - idx), abs(maxIdx - idx)))
            elif idx > minIdx and maxIdx == -1:
                res.append(abs(minIdx - idx))
        return res


print(Solution().shortestToChar("loveleetcode", 'e'))  # [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
