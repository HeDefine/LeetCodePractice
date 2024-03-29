#!/usr/bin/env python3

# https://leetcode-cn.com/problems/length-of-last-word
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l0 = s.split(" ")
        l0.reverse()
        for s in l0:
            if len(s) == 0:
                continue
            else:
                return len(s)
        return 0


print(Solution().lengthOfLastWord("Hello World"))
print(Solution().lengthOfLastWord("a "))
print(Solution().lengthOfLastWord(""))
print(Solution().lengthOfLastWord("  a "))
