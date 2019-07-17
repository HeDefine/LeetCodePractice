#!/usr/bin/env python3

# https://leetcode-cn.com/problems/longest-common-prefix
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#


class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        result = ""
        for idx, s in enumerate(strs):
            if idx == 0:
                result = s
                continue
            temp = ""
            for idx, ch in enumerate(result):
                if idx >= len(s):
                    break
                if ch != s[idx]:
                    break
                temp = temp + ch
            result = temp
        return result


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))  # ""


# 解题思路: 两次遍历，时间复杂度O(n^2)  一次遍历字符串，一次遍历前面重复几个字符串重复的前缀
