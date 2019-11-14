#!/usr/bin/env python3

# https://leetcode-cn.com/problems/add-and-search-word-data-structure-design
# 设计一个支持以下两种操作的数据结构：
# void addWord(word)
# bool search(word)
# search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
#
# 示例:
#
# 说明:
# 你可以假设所有单词都是由小写字母 a-z 组成的。


class WordDictionary:

    def __init__(self):
        import collections
        self.wordCollection = collections.defaultdict(list)

    def addWord(self, word: str) -> None:
        self.wordCollection[len(word)] += [word]
        print(word)

    def search(self, word: str) -> bool:
        def f(s):
            for i in range(len(word)):
                if word[i] not in {s[i], '.'}:
                    return False
            return True

        for s in self.wordCollection[len(word)]:
            if f(s):
                return True
        return False


param_2 = WordDictionary()
print(param_2.addWord("1234"))

# print(param_2.addWord("dad"))
# print(param_2.addWord("mad"))
# print(param_2.search("pad"))  # false
# print(param_2.search("bad"))  # true
# print(param_2.search(".ad"))  # true
# print(param_2.search("b.."))  # true


param_3 = WordDictionary()
# print(param_3.addWord('at'))
# print(param_3.addWord('and'))
# print(param_3.addWord('an'))
# print(param_3.addWord('add'))
# print(param_3.search('a'))
# print(param_3.search('.at'))
# print(param_3.addWord('bat'))
# print(param_3.search('.at'))
# print(param_3.search('an.'))
# print(param_3.search('a.d.'))
# print(param_3.search('b.'))
# print(param_3.search('a.d'))
# print(param_3.search('.'))
