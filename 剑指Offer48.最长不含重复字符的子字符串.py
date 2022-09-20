# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
#  
# 示例 1:
# 输入: "abcabcbb"  
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 提示：
# s.length <= 40000

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx, res = 0, 1
        while idx + res <= len(s):
            temp = s[idx:idx + res]
            if len(set(temp)) == len(temp):
                res += 1
            else:
                idx += 1
        return res - 1

print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('bbbbbbb'))
print(Solution().lengthOfLongestSubstring('pwwkew'))
print(Solution().lengthOfLongestSubstring(' '))
print(Solution().lengthOfLongestSubstring(''))
        