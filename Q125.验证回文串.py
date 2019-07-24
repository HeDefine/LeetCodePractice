#!/usr/bin/env python3

# https://leetcode-cn.com/problems/valid-palindrome
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i <= j:
            v1 = s[i]
            v2 = s[j]

            if v1 == v2:
                i += 1
                j -= 1
            else:
                if not v1.islower() and not v1.isdigit():
                    i += 1
                    continue
                elif not v2.islower() and not v2.isdigit():
                    j -= 1
                    continue
                else:
                    return False

        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))  # True
print(Solution().isPalindrome("race a car"))  # False

# 题解: 二分法
