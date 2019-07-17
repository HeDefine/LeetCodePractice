#!/usr/bin/env python3

# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        count_max = 1
        re = []
        for i in range(len(s)):
            if s[i] in re:
                re = re[re.index(s[i]) + 1:]
                re.append(s[i])
            else:
                re.append(s[i])
                if len(re) > count_max:
                    count_max = len(re)
            print(s[i], re)

        return count_max


print(Solution().lengthOfLongestSubstring("abcabcbb"))

# 解题思路: 这里用了拼接的方法,一个字符一个字符移动过去。遇到重复的，从重复的地方开始重新算起

# 我原先的想法是最暴力的。获取所有的子字符串，然后查找字符串是否有重复的字符
