#!/usr/bin/env python3

# https://leetcode-cn.com/problems/convert-bst-to-greater-tree
# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
#
# 例如：
# 输入: 二叉搜索树:
#               5
#             /   \
#            2     13
#          /      /  \
#         1      12  18
# 输出: 转换为累加树:
#              18
#             /   \
#           20     13


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def getAllTree(r: TreeNode) -> [TreeNode]:
            if r is None:
                return []
            return getAllTree(r.right) + [r] + getAllTree(r.left)

        temp = getAllTree(root)
        for idx in range(len(temp)):
            if idx >= 1:
                temp[idx].val += temp[idx-1].val

        return root


T0 = TreeNode(5)
T1 = TreeNode(2)
T2 = TreeNode(13)
# T4 = TreeNode(1)
# T5 = TreeNode(12)
# T6 = TreeNode(18)

T0.left = T1
T0.right = T2
# T1.left = T4
# T2.left = T5
# T2.right = T6

r = Solution().convertBST(T0)
print(r.val)
print(r.left.val)
print(r.right.val)
