#!/usr/bin/env python3

# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.
#
# 示例 1:
# 输入:
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 输出: [3, 14.5, 11]
# 解释:
# 第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
#
# 注意：
# 节点值的范围在32位有符号整数范围内。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> [float]:
        countDic = dict()
        sumDic = dict()
        resDic = dict()

        def eachLevel(r: TreeNode, level: int):
            if r is not None:
                countDic[level] = countDic.get(level, 0) + 1
                sumDic[level] = sumDic.get(level, 0) + r.val
                if sumDic[level] != 0:
                    resDic[level] = sumDic[level] / countDic[level]
                else:
                    resDic[level] = 0
                eachLevel(r.left, level + 1)
                eachLevel(r.right, level + 1)

        eachLevel(root, 0)
        return list(resDic.values())


T1 = TreeNode(3)
T2 = TreeNode(9)
T3 = TreeNode(20)
T4 = TreeNode(15)
T5 = TreeNode(7)
T1.left = T2
T1.right = T3
T3.left = T4
T3.right = T5

print(Solution().averageOfLevels(T1))
