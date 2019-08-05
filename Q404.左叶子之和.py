#!/usr/bin/env python3

# https://leetcode-cn.com/problems/sum-of-left-leaves
# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is not None:
            if root.left is None and root.right is None:
                return 0
            elif root.left is not None and root.right is not None:
                if root.left.left is None and root.left.right is None:
                    return root.left.val + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
                else:
                    return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
            elif root.left is not None:
                if root.left.left is None and root.left.right is None:
                    return root.left.val + self.sumOfLeftLeaves(root.left)
                else:
                    return self.sumOfLeftLeaves(root.left)
            else:
                return self.sumOfLeftLeaves(root.right)
        else:
            return 0


t3 = TreeNode(3)
t9 = TreeNode(9)
t20 = TreeNode(20)
t15 = TreeNode(15)
t7 = TreeNode(7)

t3.left = t9
t3.right = t20
t20.left = t15
t20.right = t7




print(Solution().sumOfLeftLeaves(t3))
