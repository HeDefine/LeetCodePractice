#!/usr/bin/env python3

# https://leetcode-cn.com/problems/word-break
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 说明：
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
#
# 示例 1：
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
#
# 示例 2：
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
#
# 示例 3：
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false


class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        def recursion(cur: str) -> bool:
            if len(cur) == 0:
                return True
            if res.get(cur) is not None:
                return res[cur]
            for idx in range(1, len(cur) + 1):
                if cur[:idx] in wordSet and recursion(cur[idx:]):
                    res[cur] = True
                    return True
            res[cur] = False
            return False

        wordSet = set(wordDict)
        res = dict()
        return recursion(s)


# print(Solution().wordBreak("leetcode", ["leet", "code"]))
# print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))  # True
# print(Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"]))  # True
# print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))  # False
# print(Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"]))  # True
print(Solution().wordBreak("goalspecial", ["go", "goal", "goals", "special"]))
print(Solution().wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
