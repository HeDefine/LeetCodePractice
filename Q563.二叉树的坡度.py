#!/usr/bin/env python3

# https://leetcode-cn.com/problems/binary-tree-tilt
# 给定一个二叉树，计算整个树的坡度。
# 一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。
# 整个树的坡度就是其所有节点的坡度之和。
#
# 示例:
# 输入:
#          1
#        /   \
#       2     3
# 输出: 1
#
# 解释:
# 结点的坡度 2 : 0
# 结点的坡度 3 : 0
# 结点的坡度 1 : |2-3| = 1
# 树的坡度 : 0 + 0 + 1 = 1
#
# 注意:
# 1.任何子树的结点的和不会超过32位整数的范围。
# 2.坡度的值不会超过32位整数的范围。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def coverTree(r: TreeNode) -> int:
            if r is None:
                return 0
            return coverTree(r.left) + coverTree(r.right) + r.val
        if root is None:
            return 0
        return abs(coverTree(root.left) - coverTree(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)


