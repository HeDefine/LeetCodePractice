# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
# 输入为三个整数：day、month 和 year，分别表示日、月、年。
# 您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。

# 示例 1：
# 输入：day = 31, month = 8, year = 2019
# 输出："Saturday"

# 示例 2：
# 输入：day = 18, month = 7, year = 1999
# 输出："Sunday"

# 示例 3：
# 输入：day = 15, month = 8, year = 1993
# 输出："Sunday"

# 提示：
# 给出的日期一定是在 1971 到 2100 年之间的有效日期。

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = 0
        for iYear in range(1971, year):
            if (iYear % 4 == 0 and iYear % 100 != 0) or (iYear % 400 == 0):
                days += 366
            else:
                days += 365
        sMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for iMonth in range(1, month):
            days += sMonth[iMonth-1]
            if iMonth == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    days += 1
        days += (day-1)
        weeks = ["Sunday", "Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        print(days)
        # 1971,1,1 Friday
        return weeks[(days + 5) % 7]
    
print(Solution().dayOfTheWeek(31, 8, 2019))     # Saturday
print(Solution().dayOfTheWeek(18, 7, 1999))     # Sunday
# print(Solution().dayOfTheWeek(15, 8, 1993))     # Sunday
