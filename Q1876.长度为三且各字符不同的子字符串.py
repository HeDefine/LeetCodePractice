# 如果一个字符串不含有任何重复字符，我们称这个字符串为 好 字符串。
# 给你一个字符串 s ，请你返回 s 中长度为 3 的 好子字符串 的数量。
# 注意，如果相同的好子字符串出现多次，每一次都应该被记入答案之中。
# 子字符串 是一个字符串中连续的字符序列。
#  
# 示例 1：
# 输入：s = "xyzzaz"
# 输出：1
# 解释：总共有 4 个长度为 3 的子字符串："xyz"，"yzz"，"zza" 和 "zaz" 。
# 唯一的长度为 3 的好子字符串是 "xyz" 。
#  
# 示例 2：
# 输入：s = "aababcabc"
# 输出：4
# 解释：总共有 7 个长度为 3 的子字符串："aab"，"aba"，"bab"，"abc"，"bca"，"cab" 和 "abc" 。
# 好子字符串包括 "abc"，"bca"，"cab" 和 "abc" 。
#  
# 提示：
# 1 <= s.length <= 100
# s​​​​​​ 只包含小写英文字母。

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        res = 0
        temp = [-1, s[0], s[1]]
        for idx in range(len(s)-2):
            temp.pop(0)
            temp.append(s[idx+2])
            if temp[0] != temp[1] and temp[0] != temp[2] and temp[1] != temp[2]:
                res += 1
        return res

print(Solution().countGoodSubstrings(s = "xyzzaz")) # 1
print(Solution().countGoodSubstrings(s = "aababcabc"))  # 4