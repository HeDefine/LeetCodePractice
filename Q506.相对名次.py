#!/usr/bin/env python3

# https://leetcode-cn.com/problems/relative-ranks
# 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。
# (注：分数越高的选手，排名越靠前。)
#
# 示例 1:
# 输入: [5, 4, 3, 2, 1]
# 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# 解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
# 余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
#
# 提示:
# N 是一个正整数并且不会超过 10000。
# 所有运动员的成绩都不相同。


class Solution:
    def findRelativeRanks(self, nums: [int]) -> [str]:
        dic = dict()
        result = list()
        for idx, num in enumerate(nums):
            dic[num] = idx
            result.append("")

        li = sorted(dic.keys(), reverse=True)
        for i, key in enumerate(li):
            idx = dic[key]
            if i == 0:
                result[idx] = "Gold Medal"
            elif i == 1:
                result[idx] = "Silver Medal"
            elif i == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(i + 1)
        return result


print(Solution().findRelativeRanks([5, 4, 3, 2, 1]))  # ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
print(Solution().findRelativeRanks(
    [39, 21, 33, 11, 23, 3, 4, 12]))  # ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
print(Solution().findRelativeRanks([1]))
