#!/usr/bin/env python3

# https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists
# 假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
# 你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。
#
# 示例 1:
# 输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# 输出: ["Shogun"]
# 解释: 他们唯一共同喜爱的餐厅是“Shogun”。
#
# 示例 2:
# 输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# 输出: ["Shogun"]
# 解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
#
# 提示:
# 1.两个列表的长度范围都在 [1, 1000]内。
# 2.两个列表中的字符串的长度将在[1，30]的范围内。
# 3.下标从0开始，到列表的长度减1。
# 4.两个列表都没有重复的元素。


class Solution:
    def findRestaurant(self, list1: [str], list2: [str]) -> [str]:
        dic = dict()
        minV = (len(list1) + len(list2), [])
        for idx, s in enumerate(list1):
            dic[s] = idx
        for idx, s in enumerate(list2):
            if dic.get(s) is not None:
                if minV[0] > idx + dic[s]:
                    minV = (idx + dic[s], [s])
                elif minV[0] == idx + dic[s]:
                    minV[1].append(s)
        return minV[1]


print(Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                                ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse",
                                 "Shogun"]))  # [Shogun]
print(Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                                ["KFC", "Shogun", "Burger King"]))  # ["Shogun"]
