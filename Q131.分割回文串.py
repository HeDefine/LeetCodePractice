#!/usr/bin/env python3

# https://leetcode-cn.com/problems/palindrome-partitioning
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 返回 s 所有可能的分割方案。
#
# 示例:
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]


class Solution:
    def partition(self, s: str) -> [[str]]:
        def recursion(cur: [], leftStr: str):
            if len(leftStr) == 0:
                res.append(cur)

            for i in range(1, len(leftStr) + 1):
                t = leftStr[:i]
                if t == t[::-1]:
                    recursion(cur + [leftStr[:i]], leftStr[i:])

        res = list()
        recursion([], s)
        return res


print(Solution().partition("aab"))
