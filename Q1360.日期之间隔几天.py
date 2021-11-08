# 请你编写一个程序来计算两个日期之间隔了多少天。
# 日期以字符串形式给出，格式为 YYYY-MM-DD，如示例所示。
#  
# 示例 1：
# 输入：date1 = "2019-06-29", date2 = "2019-06-30"
# 输出：1
#
# 示例 2：
# 输入：date1 = "2020-01-15", date2 = "2019-12-31"
# 输出：15
#  
# 提示：
# 给定的日期是 1971 年到 2100 年之间的有效日期。

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def daysFrom1971(dateStr:str) -> int:
            res = 0
            year = int(dateStr[:4])
            month = int(dateStr[5:7])
            day = int(dateStr[8:10])
            for cur_year in range(1971, year):
                res += 365
                if (cur_year % 4 == 0 and cur_year % 100 != 0) or cur_year % 400 == 0:
                    res += 1
            months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            for cur_month in range(0, month):
                res += months[cur_month]
            res += day
            return res
        
        date1_day = daysFrom1971(date1)
        date2_day = daysFrom1971(date2)
        return abs(date1_day - date2_day)
    
print(Solution().daysBetweenDates(date1 = "2019-06-29", date2 = "2019-06-30"))  # 1
print(Solution().daysBetweenDates(date1 = "2020-01-15", date2 = "2019-12-31"))  # 15