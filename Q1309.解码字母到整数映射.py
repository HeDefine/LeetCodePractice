# 给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：
# 字符（'a' - 'i'）分别用（'1' - '9'）表示。
# 字符（'j' - 'z'）分别用（'10#' - '26#'）表示。 
# 返回映射之后形成的新字符串。
# 题目数据保证映射始终唯一。
#  
# 示例 1：
# 输入：s = "10#11#12"
# 输出："jkab"
# 解释："j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
#
# 示例 2：
# 输入：s = "1326#"
# 输出："acz"
#
# 示例 3：
# 输入：s = "25#"
# 输出："y"
#
# 示例 4：
# 输入：s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
# 输出："abcdefghijklmnopqrstuvwxyz"
#  
# 提示：
# 1 <= s.length <= 1000
# s[i] 只包含数字（'0'-'9'）和 '#' 字符。
# s 是映射始终存在的有效字符串

class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        idx = 0
        while idx < len(s):
            offset = 0
            if idx + 2 < len(s) and s[idx + 2] == '#':
                offset = int(s[idx:idx + 2]) 
                idx = idx + 3
            else:
                offset = int(s[idx])
                idx += 1
            res += chr(ord('a') + offset-1)
        return res
        
            
        
    
print(Solution().freqAlphabets('10#11#12')) # jkab
print(Solution().freqAlphabets('1326#'))    # acz
print(Solution().freqAlphabets('25#'))  # y
print(Solution().freqAlphabets('12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#')) # abcdefghijklmnopqrstuvwxyz