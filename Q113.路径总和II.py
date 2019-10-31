#!/usr/bin/env python3

# https://leetcode-cn.com/problems/path-sum-ii
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> [[int]]:
        def recursion(r: TreeNode, cur: [int], s: int):
            if r is not None:
                s += r.val
                if r.left is None and r.right is None and s == sum:
                    res.append(cur + [r.val])
                recursion(r.left, cur + [r.val], s)
                recursion(r.right, cur + [r.val], s)

        res = list()
        recursion(root, [], 0)
        return res


t1 = TreeNode(5)
t2 = TreeNode(4)
t3 = TreeNode(8)
t4 = TreeNode(11)
t5 = TreeNode(13)
t6 = TreeNode(4)
t7 = TreeNode(7)
t8 = TreeNode(2)
t9 = TreeNode(5)
t10 = TreeNode(1)
t1.left = t2
t1.right = t3
t2.left = t4
t3.left = t5
t3.right = t6
t4.left = t7
t4.right = t8
t6.left = t9
t6.right = t10
print(Solution().pathSum(t1, 22))
