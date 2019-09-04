#!/usr/bin/env python3

# https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60
# 在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
# 返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字  i < j 且有 (time[i] + time[j]) % 60 == 0。
#
# 示例 1：
# 输入：[30,20,150,100,40]
# 输出：3
# 解释：这三对的总持续时间可被 60 整数：
# (time[0] = 30, time[2] = 150): 总持续时间 180
# (time[1] = 20, time[3] = 100): 总持续时间 120
# (time[1] = 20, time[4] = 40): 总持续时间 60
#
# 示例 2：
# 输入：[60,60,60]
# 输出：3
# 解释：所有三对的总持续时间都是 120，可以被 60 整数。
#  
# 提示：
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500


class Solution:
    def numPairsDivisibleBy60(self, time: [int]) -> int:
        temp = dict()
        res = 0
        for t in time:
            mod = t % 60
            res += temp.get(60 - mod if mod > 0 else 0, 0)
            temp[mod] = temp.get(mod, 0) + 1
        return res


print(Solution().numPairsDivisibleBy60([30, 20, 150, 100, 40]))  # 3
print(Solution().numPairsDivisibleBy60([60, 60, 60]))  # 3
