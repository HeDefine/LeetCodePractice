#!/usr/bin/env python3

# https://leetcode-cn.com/problems/two-city-scheduling
# 公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。
# 返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。
#
# 示例：
# 输入：[[10,20],[30,200],[400,50],[30,20]]
# 输出：110
# 解释：
# 第一个人去 A 市，费用为 10。
# 第二个人去 A 市，费用为 30。
# 第三个人去 B 市，费用为 50。
# 第四个人去 B 市，费用为 20。
#
# 最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
#
# 提示：
# 1 <= costs.length <= 100
# costs.length 为偶数
# 1 <= costs[i][0], costs[i][1] <= 1000


class Solution:
    def twoCitySchedCost(self, costs: [[int]]) -> int:
        sumA = 0
        for cost in costs:
            sumA += cost[0]

        # sumA - A + B = sumA - (A - B)
        # A - B 最大的时候 sum最小
        sortCost = sorted(costs, key=lambda x: x[0] - x[1], reverse=True)
        for i in range(len(sortCost) // 2):
            sumA = sumA - sortCost[i][0] + sortCost[i][1]
        return sumA


print(Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))  # 110
