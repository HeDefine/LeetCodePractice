# 请你设计一个可以解释字符串 command 的 Goal 解析器 。
# command 由 "G"、"()" 和/或 "(al)" 按某种顺序组成。
# Goal 解析器会将 "G" 解释为字符串 "G"、"()" 解释为字符串 "o" ，"(al)" 解释为字符串 "al" 。
# 然后，按原顺序将经解释得到的字符串连接成一个字符串。
# 给你字符串 command ，返回 Goal 解析器 对 command 的解释结果。
#  
# 示例 1：
# 输入：command = "G()(al)"
# 输出："Goal"
# 解释：Goal 解析器解释命令的步骤如下所示：
# G -> G
# () -> o
# (al) -> al
# 最后连接得到的结果是 "Goal"
#  
# 示例 2：
# 输入：command = "G()()()()(al)"
# 输出："Gooooal"
#  
# 示例 3：
# 输入：command = "(al)G(al)()()G"
# 输出："alGalooG"
#  
# 提示：
# 1 <= command.length <= 100
# command 由 "G"、"()" 和/或 "(al)" 按某种顺序组成

class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        cur_idx = 0
        while cur_idx < len(command):
            val = command[cur_idx]
            print(val)
            if val == '(':
                if command[cur_idx + 1] == ')':
                    res += 'o'
                    cur_idx += 2
                else:
                    res += 'al'
                    cur_idx += 4
            else:
                res += val
                cur_idx += 1
        return res
    
print(Solution().interpret(command = "G()(al)"))    # "Goal"
print(Solution().interpret(command = "G()()()()(al)"))  # "Gooooal"
print(Solution().interpret(command = "(al)G(al)()()G")) # "alGalooG"