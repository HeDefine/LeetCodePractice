# 给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。
# 输入为 非空 字符串且只包含数字 1 和 0。
#  
# 示例 1:
# 输入: a = "11", b = "10"
# 输出: "101"
#
# 示例 2:
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#  
# 提示：
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        t = 0
        for i in range(max(len(b), len(a))):
            int_a = int(a[-i-1]) if i < len(a) else 0
            int_b = int(b[-i-1]) if i < len(b) else 0
            print(int_a, int_b)
            res = str(int_a ^ int_b ^ t) + res
            t = 1 if (int_a + int_b + t) >= 2 else 0        # 进位
        if t > 0:
            res = '1' + res
        return res
            
            
print(Solution().addBinary("11", "10"))     # 101
print(Solution().addBinary("1010", "1011")) # 10101
print(Solution().addBinary("1", "111")) # 1000
