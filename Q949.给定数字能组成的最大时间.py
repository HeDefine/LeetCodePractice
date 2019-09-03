#!/usr/bin/env python3

# https://leetcode-cn.com/problems/largest-time-for-given-digits
# 给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
# 最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。
# 以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。
#
# 示例 1：
# 输入：[1,2,3,4]
# 输出："23:41"
#
# 示例 2：
# 输入：[5,5,5,5]
# 输出：""
#
# 提示：
# A.length == 4
# 0 <= A[i] <= 9


class Solution:
    def largestTimeFromDigits(self, A: [int]) -> str:
        A.sort(reverse=True)
        for idx1, h1 in enumerate(A):
            temp1 = A[:idx1] + A[idx1 + 1:]
            for idx2, h2 in enumerate(temp1):
                temp2 = temp1[:idx2] + temp1[idx2 + 1:]
                for idx3, m1 in enumerate(temp2):
                    temp3 = temp2[:idx3] + temp2[idx3 + 1:]
                    m2 = temp3[0]
                    if m1 * 10 + m2 < 59 and (h1 * 10 + h2) * 60 + (m1 * 10 + m2) < 23 * 60 + 59:
                        return '%d%d:%d%d' % (h1, h2, m1, m2)
        return ""

print(Solution().largestTimeFromDigits([1, 2, 3, 4]))  # 23:41
print(Solution().largestTimeFromDigits([1, 2, 4, 5]))  # 23:41
print(Solution().largestTimeFromDigits([0, 1, 1, 2]))
print(Solution().largestTimeFromDigits([5, 5, 5, 5]))  # ''
print(Solution().largestTimeFromDigits([0, 1, 1, 1]))
print(Solution().largestTimeFromDigits([0, 0, 1, 0]))  # "10:00"
print(Solution().largestTimeFromDigits([0, 2, 2, 3]))
print(Solution().largestTimeFromDigits([4, 2, 4, 4]))
print(Solution().largestTimeFromDigits([1, 9, 6, 0]))
