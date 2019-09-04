#!/usr/bin/env python3

# https://leetcode-cn.com/problems/find-common-characters
# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
# 例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
# 你可以按任意顺序返回答案。
#
# 示例 1：
# 输入：["bella","label","roller"]
# 输出：["e","l","l"]
#
# 示例 2：
# 输入：["cool","lock","cook"]
# 输出：["c","o"]
#
# 提示：
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] 是小写字母


class Solution:
    def commonChars(self, A: [str]) -> [str]:
        temp = set()
        count = dict()
        for idx, word in enumerate(A):
            if len(temp) == 0:
                temp = set(word)
            else:
                temp = temp.intersection(set(word))
            if len(temp) == 0:
                return []
            dic = dict()
            for ch in word:
                if ch in temp:
                    dic[ch] = dic.get(ch, 0) + 1
            if idx > 0:
                # print(dic, count, temp)
                for ch, num in dic.items():
                    dic[ch] = min(count[ch], num)
            count = dic
        res = list()
        for i in temp:
            res += [i] * count[i]
        return res


# print(Solution().commonChars(["bella", "label", "roller"]))  # ["e","l","l"]
# print(Solution().commonChars(["cool", "lock", "cook"]))  # ["c","o"]
print(Solution().commonChars(
    ["acabcddd", "bcbdbcbd", "baddbadb", "cbdddcac", "aacbcccd", "ccccddda", "cababaab", "addcaccd"]))
