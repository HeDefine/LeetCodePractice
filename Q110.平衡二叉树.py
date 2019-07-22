#!/usr/bin/env python3

# https://leetcode-cn.com/problems/balanced-binary-tree
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
# 示例 1:
# 给定二叉树 [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。
#
# 示例 2:
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def maxDepth(tr: TreeNode) -> int:
            if tr is None:
                return 0
            return max(maxDepth(tr.left), maxDepth(tr.right)) + 1

        if root is None:
            return True
        lTreeDepth = maxDepth(root.left)
        rTreeDepth = maxDepth(root.right)
        if abs(lTreeDepth - rTreeDepth) > 1:
            return False

        return self.isBalanced(root.left) & self.isBalanced(root.right)


t0 = TreeNode(3)
t11 = TreeNode(9)
t12 = TreeNode(20)
t23 = TreeNode(15)
t24 = TreeNode(7)
t0.left = t11
t0.right = t12
t12.left = t23
t12.right = t24

print(Solution().isBalanced(t0))

# 题解，求每个左右树的最深深度
