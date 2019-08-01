#!/usr/bin/env python3

# https://leetcode-cn.com/problems/reverse-vowels-of-a-string
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1:
# 输入: "hello"
# 输出: "holle"
#
# 示例 2:
# 输入: "leetcode"
# 输出: "leotcede"
#
# 说明:
# 元音字母不包含字母"y"。


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        i = 0
        j = len(s) - 1
        li = list(s)
        while i < j:
            if li[i].lower() in vowels and li[j].lower() in vowels:
                li[i], li[j] = li[j], li[i]
                i += 1
                j -= 1
            else:
                if li[i].lower() not in vowels:
                    i += 1
                if li[j].lower() not in vowels:
                    j -= 1

        return "".join(li)


print(Solution().reverseVowels("hello"))  # "holle"
print(Solution().reverseVowels("leetcode"))  # "leotcede"
