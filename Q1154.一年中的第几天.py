#!/usr/bin/env python3

# https://leetcode-cn.com/problems/ordinal-number-of-date
# 给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。
# 通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。
# 每个月的天数与现行公元纪年法（格里高利历）一致。
#
# 示例 1：
# 输入：date = "2019-01-09"
# 输出：9
#
# 示例 2：
# 输入：date = "2019-02-10"
# 输出：41
#
# 示例 3：
# 输入：date = "2003-03-01"
# 输出：60
#
# 示例 4：
# 输入：date = "2004-03-01"
# 输出：61
#  
# 提示：
# date.length == 10
# date[4] == date[7] == '-'，其他的 date[i] 都是数字。
# date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日。


class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])

        months = [31,
                  29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28,
                  31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        return sum(months[:month - 1]) + day


print(Solution().dayOfYear(date="2019-01-09"))  # 9
print(Solution().dayOfYear(date="2019-02-10"))  # 41
print(Solution().dayOfYear(date="2003-03-01"))  # 60
print(Solution().dayOfYear(date="2004-03-01"))  # 61
