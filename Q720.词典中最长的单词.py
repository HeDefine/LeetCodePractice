#!/usr/bin/env python3

# https://leetcode-cn.com/problems/longest-word-in-dictionary
# 给出一个字符串数组words组成的一本英语词典。
# 从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。
# 若其中有多个可行的答案，则返回答案中字典序最小的单词。
# 若无答案，则返回空字符串。
#
# 示例 1:
# 输入:
# words = ["w","wo","wor","worl", "world"]
# 输出: "world"
# 解释:
# 单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
#
# 示例 2:
# 输入:
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# 输出: "apple"
# 解释:
# "apply"和"apple"都能由词典中的单词组成。但是"apple"得字典序小于"apply"。
#
# 注意:
# 所有输入的字符串都只包含小写字母。
# words数组长度范围为[1,1000]。
# words[i]的长度范围为[1,30]。


class Solution:
    def longestWord(self, words: [str]) -> str:
        words.sort()
        words.sort(key=len, reverse=True)
        set0 = set(words)
        res = ""
        for word in words:
            isCur = True
            for i in range(1, len(word) + 1):
                if word[0:i] not in set0:
                    print(False)
                    isCur = False
                    break
            if isCur:
                res = word
                break
        return res


# print(Solution().longestWord(["w", "wo", "wor", "worl", "world"]))  # "world"
print(Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))  # ""apple""
# print(Solution().longestWord(
#     ["b", "br", "bre", "brea", "break", "breakf", "breakfa", "breakfas", "breakfast", "l", "lu", "lun", "lunc", "lunch",
#      "d", "di", "din", "dinn", "dinne", "dinner"]))
print(Solution().longestWord(
    ["t", "ti", "tig", "tige", "tiger", "e", "en", "eng", "engl", "engli", "englis", "english", "h", "hi", "his",
     "hist", "histo", "histor", "history"]))
