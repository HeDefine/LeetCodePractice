#!/usr/bin/env python3

# https://leetcode-cn.com/problems/implement-trie-prefix-tree
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
#
# 说明:
# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。


class Trie:

    def __init__(self):
        self.preSet = set()
        self.wordSet = set()

    def insert(self, word: str) -> None:
        self.wordSet.add(word)
        for idx in range(len(word)):
            self.preSet.add(word[:idx + 1])

    def search(self, word: str) -> bool:
        return word in self.wordSet

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.preSet


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # 返回 true
print(trie.search("app"))  # 返回 false
print(trie.startsWith("app"))  # 返回 true
print(trie.insert("app"))
print(trie.search("app"))  # 返回 true
