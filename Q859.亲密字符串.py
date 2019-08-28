#!/usr/bin/env python3

# https://leetcode-cn.com/problems/buddy-strings
# 给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。
#
# 示例 1：
# 输入： A = "ab", B = "ba"
# 输出： true
#
# 示例 2：
# 输入： A = "ab", B = "ab"
# 输出： false
#
# 示例 3:
# 输入： A = "aa", B = "aa"
# 输出： true
#
# 示例 4：
# 输入： A = "aaaaaaabc", B = "aaaaaaacb"
# 输出： true
#
# 示例 5：
# 输入： A = "", B = "aa"
# 输出： false
#
# 提示：
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A 和 B 仅由小写字母构成。


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) == len(B) == 0:
            return False
        if A == B and len(set(A)) < len(A):
            return True
        firstIdx = 0
        lastIdx = len(A) - 1
        while firstIdx <= lastIdx:
            if A[firstIdx] != B[firstIdx] and A[lastIdx] != B[lastIdx]:
                break
            if A[firstIdx] == B[firstIdx]:
                firstIdx += 1
            if A[lastIdx] == B[lastIdx]:
                lastIdx -= 1

        tempA = list(A)
        tempA[firstIdx], tempA[lastIdx] = tempA[lastIdx], tempA[firstIdx]
        res = "".join(tempA)
        return res == B


print(Solution().buddyStrings("ab", "ba"))  # True
print(Solution().buddyStrings("ab", "ab"))  # False
print(Solution().buddyStrings("aa", "aa"))  # True
print(Solution().buddyStrings("aaaaaaabc", "aaaaaaacb"))  # True
print(Solution().buddyStrings("", "aa"))  # False
