#!/usr/bin/env python3

# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
# 给定一个二叉树，原地将它展开为链表。
# 例如，给定二叉树
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        def recursion(r: TreeNode) -> (TreeNode, TreeNode):
            if r is not None:
                tempL = recursion(r.left)
                tempR = recursion(r.right)
                r.left = None
                if tempL[0] and tempL[1] and tempR[0] and tempR[1]:
                    tempL[1].right = tempR[0]
                    r.right = tempL[0]
                    return r, tempR[1]
                if tempL[0] and tempL[1] and not tempR[0] and not tempR[1]:
                    r.right = tempL[0]
                    return r, tempL[1]
                return r, tempR[1] if tempR[1] else r
            return None, None
        recursion(root)


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t1.left = t2
t1.right = t5
t2.left = t3
t2.right = t4
t5.right = t6

Solution().flatten(t1)
while t1 is not None:
    print(t1.val)
    t1 = t1.right
