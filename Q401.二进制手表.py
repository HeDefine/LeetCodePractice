#!/usr/bin/env python3

# https://leetcode-cn.com/problems/binary-watch
# 二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。
# 每个 LED 代表一个 0 或 1，最低位在右侧。
# 给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。
#
# 案例:
# 输入: n = 1
# 返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
#  
# 注意事项:
# 输出的顺序没有要求。
# 小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
# 分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。


class Solution:
    def __init__(self):
        self.allResultDic = dict()
        for h in range(12):
            for m in range(60):
                s = str(bin(h))[2:] + str(bin(m))[2:]
                count = s.count("1")
                val = "%d:%2d" % (h, m)
                if self.allResultDic.get(count) is None:
                    self.allResultDic[count] = [val]
                else:
                    self.allResultDic[count].append(val)

    def readBinaryWatch(self, num: int) -> [str]:
        return self.allResultDic.get(num)



print(Solution().readBinaryWatch(1))  # ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
