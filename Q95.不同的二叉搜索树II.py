#!/usr/bin/env python3

# https://leetcode-cn.com/problems/unique-binary-search-trees-ii
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
#
# 示例:
# 输入: 3
# 输出:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释:
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> [TreeNode]:
        def cover(beginIdx: int, endIdx: int) -> [TreeNode]:
            if beginIdx > endIdx:
                return [None, ]

            temp = []
            for i in range(beginIdx, endIdx + 1):
                leftTrees = cover(beginIdx, i - 1)
                rightTrees = cover(i + 1, endIdx)
                for lT in leftTrees:
                    for rT in rightTrees:
                        curTree = TreeNode(i)
                        curTree.left = lT
                        curTree.right = rT
                        temp.append(curTree)
            return temp

        if n:
            return cover(1, n)
        else:
            return []


t = (Solution().generateTrees(3))
print(len(t))
