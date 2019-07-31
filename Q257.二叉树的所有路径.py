#!/usr/bin/env python3

# https://leetcode-cn.com/problems/binary-tree-paths
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
# 示例:
# 输入:
#    1
#  /   \
# 2     3
#  \
#   5
#
# 输出: ["1->2->5", "1->3"]
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> [str]:
        pass

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t2.right = t5

print(Solution().binaryTreePaths(t1))  # ["1->2->5", "1->3"]
