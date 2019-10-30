#!/usr/bin/env python3

# https://leetcode-cn.com/problems/restore-ip-addresses
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 示例:
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]


class Solution:
    def restoreIpAddresses(self, s: str) -> [str]:
        def cover(cur: [], left: str):
            if len(left) <= (4 - len(cur)) * 3:
                if len(cur) == 4 and len(left) == 0:
                    res.append('.'.join(cur))
                else:
                    if len(left) > 0 and left[0] == '0':
                        cover(cur + ['0'], left[1:])
                        return
                    for idx, val in enumerate(left):
                        if idx < 3:
                            piece = left[:idx + 1]
                            if 0 <= int(piece) <= 255:
                                cover(cur + [piece], left[idx + 1:])

        res = list()
        cover([], s)
        return res


print(Solution().restoreIpAddresses("25525511135"))
print(Solution().restoreIpAddresses("010010"))  # ["0.10.0.10","0.100.1.0"]
