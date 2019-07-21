#!/usr/bin/env python3

# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


t0 = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
t3 = TreeNode(15)
t4 = TreeNode(7)

t0.left = t1
t0.right = t2
t2.left = t3
t2.right = t4

print(Solution().maxDepth(t0))  # 3


# 题解: 求二叉树的深度，没什么好讲的
