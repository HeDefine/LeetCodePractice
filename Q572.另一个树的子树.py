#!/usr/bin/env python3

# https://leetcode-cn.com/problems/subtree-of-another-tree
# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。
#
# 示例 1:
# 给定的树 s:
#      3
#     / \
#    4   5
#   / \
#  1   2
# 给定的树 t：
#    4
#   / \
#  1   2
# 返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
#
# 示例 2:
# 给定的树 s：
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# 给定的树 t：
#    4
#   / \
#  1   2
# 返回 false。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(t0: TreeNode, t1: TreeNode):
            if t0 is None and t1 is None:
                return True
            elif t0 is not None and t1 is not None:
                return isSame(t0.left, t1.left) and isSame(t0.right, t1.right) and t0.val == t1.val
            else:
                return False
        if s is None:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) or isSame(s, t)
