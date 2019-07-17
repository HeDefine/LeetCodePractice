#!/usr/bin/env python3

# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"


class Solution:
    # 方法1和方法2 不完整。因为没有考虑到偶数位的对称。

    # 方法1  递归。 但是测试结果表示,超过了递归的深度
    def longestPalindrome(self, s: str) -> str:
        maxString = ""
        for (idx, ch) in enumerate(s):
            palindromeStr = self.checkIsPalindrome(s, idx, 0)
            if len(palindromeStr) >= len(maxString):
                maxString = palindromeStr
        return maxString

    def checkIsPalindrome(self, s: str, mid: int, offset: int):
        offset1 = mid - offset
        offset2 = mid + offset
        ch1 = ""
        ch2 = ""
        if offset1 >= 0:
            ch1 = s[offset1]

        if offset2 < len(s):
            ch2 = s[offset2]

        if ch1 != ch2:
            return s[offset1 + 1: offset2]
        else:
            return self.checkIsPalindrome(s, mid, offset + 1)

    # 方法2 循环.在上面的基础上做修改
    def longestPalindrome2(self, s: str) -> str:
        maxString = ""
        for (idx, ch) in enumerate(s):
            palindromeStr = ""
            for offset in range(len(s)):
                ch1 = ""
                ch2 = ""
                if idx - offset >= 0:
                    ch1 = s[idx - offset]
                if idx + offset < len(s):
                    ch2 = s[idx + offset]
                if ch1 != ch2:
                    palindromeStr = s[idx - offset + 1: idx + offset]
                    break
                offset += 1

            if len(palindromeStr) >= len(maxString):
                maxString = palindromeStr
        return maxString

    # 做到这里的时候提交，发现方法1和方法2 不完整。因为没有考虑到是偶数位的情况。因此在做完善
    # 中间相同的去除
    def longestPalindrome3(self, s: str) -> str:
        maxString = ""
        for (idx, ch) in enumerate(s):
            palindromeStr = s[0]
            offset1 = idx - 1
            offset2 = idx + 1
            isExtend = True
            for i in range(len(s)):
                ch1 = ""
                ch2 = ""
                # print(offset1, offset2)
                if offset1 >= 0:
                    ch1 = s[offset1]
                    if ch1 == ch and isExtend:
                        offset1 -= 1
                        continue
                else:
                    palindromeStr = s[offset1+1: offset2]
                    break

                if offset2 < len(s):
                    ch2 = s[offset2]
                    if ch2 == ch and isExtend:
                        offset2 += 1
                        if offset2 + 1 < len(s):
                            continue
                else:
                    palindromeStr = s[offset1+1: offset2]
                    break

                isExtend = False
                if ch1 != ch2:
                    palindromeStr = s[offset1+1: offset2]
                    break
                offset1 -= 1
                offset2 += 1
            if len(palindromeStr) >= len(maxString):
                maxString = palindromeStr
        return maxString


print(Solution().longestPalindrome2("babad"))
# print(Solution().longestPalindrome3("caaaaddasdaaaacccc"))
# print(Solution().longestPalindrome3("bbb"))
# print(Solution().longestPalindrome3("aba"))
