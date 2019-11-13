#!/usr/bin/env python3

# https://leetcode-cn.com/problems/repeated-dna-sequences
# 所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
# 编写一个函数来查找 DNA 分子中所有出现超过一次的 10 个字母长的序列（子串）。
#
# 示例：
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC", "CCCCCAAAAA"]


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> [str]:
        temp = set()
        res = set()
        for idx in range(10, len(s) + 1):
            pieceStr = s[idx - 10:idx]
            if pieceStr in temp:
                res.add(pieceStr)
            temp.add(pieceStr)
        return list(res)

print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))  # ["AAAAACCCCC", "CCCCCAAAAA"]
