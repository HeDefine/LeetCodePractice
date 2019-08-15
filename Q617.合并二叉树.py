#!/usr/bin/env python3

# https://leetcode-cn.com/problems/merge-two-binary-trees
# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
# 你需要将他们合并为一个新的二叉树。
# 合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
#
# 示例 1:
# 输入:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# 输出:
# 合并后的树:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
# 注意: 合并必须从两个树的根节点开始。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        elif t1 is not None and t2 is None:
            t = TreeNode(t1.val)
            t.left = t1.left
            t.right = t1.right
            return t
        elif t1 is None and t2 is not None:
            t = TreeNode(t2.val)
            t.left = t2.left
            t.right = t2.right
            return t
        elif t1 is not None and t2 is not None:
            t = TreeNode(t1.val + t2.val)
            t.left = self.mergeTrees(t1.left, t2.left)
            t.right = self.mergeTrees(t1.right, t2.right)
            return t

