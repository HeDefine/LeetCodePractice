#!/usr/bin/env python3

# https://leetcode-cn.com/problems/uncommon-words-from-two-sentences
# 给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
# 如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
# 返回所有不常用单词的列表。
# 您可以按任何顺序返回列表。
#
# 示例 1：
# 输入：A = "this apple is sweet", B = "this apple is sour"
# 输出：["sweet","sour"]
#
# 示例 2：
# 输入：A = "apple apple", B = "banana"
# 输出：["banana"]
#
# 提示：
# 1. 0 <= A.length <= 200
# 2. 0 <= B.length <= 200
# 3. A 和 B 都只包含空格和小写字母。


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> [str]:
        temp = set()
        res = dict()
        for each in A.split(' ') + B.split(' '):
            if res.get(each) is not None:
                del res[each]
                temp.add(each)
                continue
            if each not in temp:
                res[each] = 1
        return list(res.keys())


print(Solution().uncommonFromSentences("this apple is sweet", "this apple is sour"))  # ["sweet","sour"]
print(Solution().uncommonFromSentences("apple apple", "banana"))  # ["banana"]
print(Solution().uncommonFromSentences("s z z z s", "s z ejt"))
