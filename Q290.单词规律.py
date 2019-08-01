#!/usr/bin/env python3

# https://leetcode-cn.com/problems/word-pattern
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
#
# 示例1:
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
#
# 示例 2:
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
#
# 示例 3:
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
#
# 示例 4:
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
#
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        nums = str.split(" ")
        if len(pattern) != len(nums):
            return False
        dic1 = dict()
        dic2 = dict()
        for idx in range(len(pattern)):
            if dic1.get(pattern[idx]) is None:
                dic1[pattern[idx]] = [idx]
            else:
                dic1[pattern[idx]].append(idx)

            if dic2.get(nums[idx]) is None:
                dic2[nums[idx]] = [idx]
            else:
                dic2[nums[idx]].append(idx)
        return list(dic1.values()) == list(dic2.values())


print(Solution().wordPattern("abba", "dog cat cat dog"))  # True
print(Solution().wordPattern("abba", "dog cat cat fish"))  # False
print(Solution().wordPattern("aaaa", "dog cat cat dog"))  # False
print(Solution().wordPattern("abba", "dog dog dog dog"))  # False
