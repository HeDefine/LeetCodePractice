#!/usr/bin/env python3

# https://leetcode-cn.com/problems/employee-importance
# 给定一个保存员工信息的数据结构，它包含了员工唯一的id，重要度 和 直系下属的id。
# 比如，员工1是员工2的领导，员工2是员工3的领导。
# 他们相应的重要度为15, 10, 5。
# 那么员工1的数据结构是[1, 15, [2]]，员工2的数据结构是[2, 10, [3]]，员工3的数据结构是[3, 5, []]。
# 注意虽然员工3也是员工1的一个下属，但是由于并不是直系下属，因此没有体现在员工1的数据结构中。
#
# 现在输入一个公司的所有员工信息，以及单个员工id，返回这个员工和他所有下属的重要度之和。
#
# 示例 1:
# 输入: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# 输出: 11
#
# 解释:
# 员工1自身的重要度是5，他有两个直系下属2和3，而且2和3的重要度均为3。因此员工1的总重要度是 5 + 3 + 3 = 11。
#
# 注意:
# 一个员工最多有一个直系领导，但是可以有多个直系下属
# 员工数量不超过2000。


# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: [int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: [Employee], id):
        dic = dict()
        for employee in employees:
            dic[employee.id] = (employee.importance, employee.subordinates)

        if dic.get(id) is None:
            return 0
        res = dic[id][0]
        allList = dic[id][1]
        for subId in allList:
            res += dic[subId][0]
            allList += dic[subId][1]
        return res


e1 = Employee(1, 5, [2, 3])
e2 = Employee(2, 3, [4])
e3 = Employee(3, 4, [])
e4 = Employee(4, 1, [])
print(Solution().getImportance([e1, e2, e3, e4], 1))
