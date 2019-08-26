#!/usr/bin/env python3

# https://leetcode-cn.com/problems/rotate-string
# 给定两个字符串, A 和 B。
# A 的旋转操作就是将 A 最左边的字符移动到最右边。 
# 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea'。
# 如果在若干次旋转操作之后，A 能变成B，那么返回True。
#
# 示例 1:
# 输入: A = 'abcde', B = 'cdeab'
# 输出: true
#
# 示例 2:
# 输入: A = 'abcde', B = 'abced'
# 输出: false
#
# 注意：
# A 和 B 长度不超过 100


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        lA = list(A)
        for i in range(len(lA)):
            temp = lA[0]
            lA[0] = ''
            lA.append(temp)
            newA = ''.join(lA)
            if newA == B:
                return True
            lA = list(newA)
        return False


print(Solution().rotateString('abcde', 'cdeab'))  # True
print(Solution().rotateString('abcde', 'abced'))  # False
