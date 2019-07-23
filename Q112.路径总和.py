#!/usr/bin/env python3

# 链接：https://leetcode-cn.com/problems/path-sum
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
# 这条路径上所有节点值相加等于目标和。
# 说明: 叶子节点是指没有子节点的节点。
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return (sum - root.val) == 0

        elif root.left is not None and root.right is not None:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

        elif root.left is not None:
            return self.hasPathSum(root.left, sum - root.val)

        else:
            return self.hasPathSum(root.right, sum - root.val)


t0 = TreeNode(5)
t10 = TreeNode(4)
t11 = TreeNode(8)
t0.left = t10
t0.right = t11

t20 = TreeNode(11)
t22 = TreeNode(13)
t23 = TreeNode(14)
t10.left = t20
t11.left = t22
t11.right = t23

t30 = TreeNode(7)
t31 = TreeNode(2)
t33 = TreeNode(1)
t20.left = t30
t20.right = t31
t23.right = t33

print(Solution().hasPathSum(t0, 22))  # true

print(Solution().hasPathSum(None, 0))

# 题解: 迭代
