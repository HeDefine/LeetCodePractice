# 给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。
#  
# 示例 1：
# 输入：s = "owoztneoer"
# 输出："012"
#  
# 示例 2：
# 输入：s = "fviefuro"
# 输出："45"
#  
# 提示：
# 1 <= s.length <= 105
# s[i] 为 ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"] 这些字符之一
# s 保证是一个符合题目要求的字符串

class Solution:
    def originalDigits(self, s: str) -> str:
        ch_count_dict = dict()
        for ch in s:
            ch_count_dict[ch] = ch_count_dict.get(ch, 0) + 1
        count_list = [0] * 10
        if ch_count_dict.get('z') is not None:
            count_list[0] = ch_count_dict['z']
        if ch_count_dict.get('w') is not None:
            count_list[2] = ch_count_dict['w']
        if ch_count_dict.get('u') is not None:
            count_list[4] = ch_count_dict['u']
        if ch_count_dict.get('x') is not None:
            count_list[6] = ch_count_dict['x']
        if ch_count_dict.get('g') is not None:
            count_list[8] = ch_count_dict['g']
        if ch_count_dict.get('o') is not None:
            count_list[1] = ch_count_dict['o'] - count_list[0] - count_list[2] - count_list[4]
        if ch_count_dict.get('t') is not None:
            count_list[3] = ch_count_dict['t'] - count_list[2] - count_list[8]
        if ch_count_dict.get('f') is not None:
            count_list[5] = ch_count_dict['f'] - count_list[4]
        if ch_count_dict.get('v') is not None:
            count_list[7] = ch_count_dict['v'] - count_list[5]
        if ch_count_dict.get('i') is not None:
            count_list[9] = ch_count_dict['i'] - count_list[5] - count_list[6] - count_list[8]
        print(count_list)
        return ''.join([str(idx) * val for idx, val in enumerate(count_list)])

print(Solution().originalDigits(s = "owoztneoer"))  # 012
print(Solution().originalDigits(s = "fviefuro"))    # 45
print(Solution().originalDigits(s = "zerozero"))    # 45
print(Solution().originalDigits("owoztneoer"))
print(Solution().originalDigits("zeroonetwothreefourfivesixseveneightnine"))

print(Solution().originalDigits("xsi"))