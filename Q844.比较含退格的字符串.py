#!/usr/bin/env python3

# https://leetcode-cn.com/problems/backspace-string-compare
# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
#
# 示例 1：
# 输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
#
# 示例 2：
# 输入：S = "ab##", T = "c#d#"
# 输出：true
# 解释：S 和 T 都会变成 “”。
#
# 示例 3：
# 输入：S = "a##c", T = "#a#c"
# 输出：true
# 解释：S 和 T 都会变成 “c”。
#
# 示例 4：
# 输入：S = "a#c", T = "b"
# 输出：false
# 解释：S 会变成 “c”，但 T 仍然是 “b”。


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def getStr(s: str) -> str:
            temp = list()
            for idx, ch in enumerate(s):
                if ch == '#':
                    if len(temp) > 0:
                        temp.pop()
                else:
                    temp.append(ch)
            return ''.join(temp)
        newS = getStr(S)
        newT = getStr(T)
        return newS == newT
print(Solution().backspaceCompare("ab#c", "ad#c"))  # True
print(Solution().backspaceCompare("ab##", "c#d#"))  # True
print(Solution().backspaceCompare("a##c", "#a#c"))  # True
print(Solution().backspaceCompare("a#c", "b"))  # False
