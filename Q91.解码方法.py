#!/usr/bin/env python3

# https://leetcode-cn.com/problems/decode-ways
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
# 示例 1:
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#
# 示例 2:
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。


class Solution:
    def numDecodings(self, s: str) -> int:
        res = [1]
        for idx, ch in enumerate(s):
            if idx == 0:
                if ch == '0':
                    return 0
                else:
                    res.append(1)
            else:
                v = int(s[idx - 1:idx + 1])
                temp = 0
                if ch != '0':
                    temp += res[-1]

                if 10 <= v <= 26:
                    temp += res[-2]

                res.append(temp)
        return res[-1]


print(Solution().numDecodings("12"))  # 2
print(Solution().numDecodings("226"))  # 3
print(Solution().numDecodings("100"))
print(Solution().numDecodings("230"))
print(Solution().numDecodings("10"))
print(Solution().numDecodings("110"))
print(Solution().numDecodings("1212"))
# print(Solution().numDecodings(
#     "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))
