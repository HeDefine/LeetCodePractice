# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
#
# 数值（按顺序）可以分成以下几个部分：
# 若干空格
# 一个 小数 或者 整数
# （可选）一个 'e' 或 'E' ，后面跟着一个 整数
# 若干空格
#
# 小数（按顺序）可以分成以下几个部分：
# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字
#
# 整数（按顺序）可以分成以下几个部分：
# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字
#
# 部分数值列举如下：
# ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
# 部分非数值列举如下：
# ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]
# 提示：
# 1 <= s.length <= 20
# s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。

class Solution:
    def isNumber(self, s: str) -> bool:
        def isInteger(temp:str) -> bool:
            if len(temp) == 0: return False
            for idx, ch in enumerate(temp):
                if ch == '+' or ch == '-':
                    if idx != 0 or len(temp) == 1:
                        return False
                elif '0' > ch or ch > '9':
                    return False
            return True

        def isDecimal(temp:str) -> bool:
            is_decimal = False
            if len(temp) > 0 and (temp[0] in ['-', '+']):
                temp = temp[1:]
            for idx, val in enumerate(temp.split('.')):
                if len(val) > 0:
                    if idx == 1 and (val[0] == '-' or val[0] == '+'):
                        return False
                    if not isInteger(val):
                        return False
                    is_decimal = is_decimal or True
                if idx > 1:
                    return False
            return is_decimal
        
        arr = s.strip().split('e')
        if 'E' in s:
            arr = s.strip().split('E')
        
        if len(arr) > 2:
            return False
        
        res = True if len(s) > 0 else False
        for idx, val in enumerate(arr):
            if idx == 0:
                res = res and isDecimal(val)
            if idx == 1:
                res = res and isInteger(val)
            
        return res

print(Solution().isNumber('+'))
print(Solution().isNumber("+.8"))
# print(Solution().isNumber('0')) # True
# print(Solution().isNumber('e')) # False
# print(Solution().isNumber('.')) # False
# print(Solution().isNumber('    .1  '))  # True
# print('---')
# for s in ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]:
#     print(Solution().isNumber(s))
# print('---')
# for s in ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]:
#     print(Solution().isNumber(s))
# print('---')    
