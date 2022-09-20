# 在字符串 s 中找出第一个只出现一次的字符。
# 如果没有，返回一个单空格。 
# s 只包含小写字母。
#
# 示例 1:
# 输入：s = "abaccdeff"
# 输出：'b'
#
# 示例 2:
# 输入：s = "" 
# 输出：' '
#  
# 限制：
# 0 <= s 的长度 <= 50000

class Solution:
    def firstUniqChar(self, s: str) -> str:
        temp = dict()
        for idx, ch in enumerate(s):
            if temp.get(ch) is not None:
                temp[ch] = len(s)
            else:
                temp[ch] =  idx
        if len(temp) == 0:
            return ' '
        min_val = min(temp, key=lambda t: temp[t])
        return min_val if temp[min_val] < len(s) else ' '

print(Solution().firstUniqChar("abaccdeff"))    # b
print(Solution().firstUniqChar("aadadaad"))    # ' '
# print(Solution().firstUniqChar(s = "" ))    # ' '