#!/usr/bin/env python3

# 链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定二叉树 [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left is not None and root.right is None:
            return self.minDepth(root.left) + 1
        elif root.left is None and root.right is not None:
            return self.minDepth(root.right) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


t0 = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
t3 = TreeNode(15)
t4 = TreeNode(7)

t0.left = t1
t0.right = t2
t2.left = t3
t2.right = t4

t10 = TreeNode(1)
t11 = TreeNode(2)
t10.right = t11
print(Solution().minDepth(t0))  # 2


# 取最小深度。递归。难度在于异常情况。还有题干里的 "叶子节点是指没有子节点的节点。"
