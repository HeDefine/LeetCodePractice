#!/usr/bin/env python3

# https://leetcode-cn.com/problems/permutation-sequence
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。
#
# 说明：
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
#
# 示例 1:
# 输入: n = 3, k = 3
# 输出: "213"
#
# 示例 2:
# 输入: n = 4, k = 9
# 输出: "2314"


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        allInt = [str(i) for i in range(1, n + 1)]
        allPurpose = [1]
        for i in range(1, n - 1):
            allPurpose = [allPurpose[0] * (i + 1)] + allPurpose

        res = ''
        for purpose in allPurpose:
            idx = (k - 1) // purpose
            res += str(allInt.pop(idx))
            k = k % purpose
        res += ''.join(allInt)
        return res


print(Solution().getPermutation(n=3, k=3))  # 213
print(Solution().getPermutation(n=4, k=9))  # 2314
