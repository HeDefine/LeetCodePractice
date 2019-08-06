#!/usr/bin/env python3

# https://leetcode-cn.com/problems/path-sum-iii
# 给定一个二叉树，它的每个结点都存放着一个整数值。
# 找出路径和等于给定数值的路径总数。
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
#
# 示例：
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
# 返回 3。和等于 8 的路径有:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        def countPath(r: TreeNode, s: int) -> int:
            if r is None:
                return 0
            res = 1 if s == r.val else 0
            return res + countPath(r.left, s - r.val) + countPath(r.right, s - r.val)

        if root is None:
            return 0

        return self.pathSum(root.left, sum) + self.pathSum(root.right, sum) + countPath(root, sum)


t1 = TreeNode(10)
t21 = TreeNode(5)
t22 = TreeNode(-3)
t1.left = t21
t1.right = t22
t31 = TreeNode(3)
t32 = TreeNode(2)
t33 = TreeNode(11)
t21.left = t31
t21.right = t32
t22.right = t33
t41 = TreeNode(3)
t42 = TreeNode(-2)
t43 = TreeNode(1)
t31.left = t41
t31.right = t42
t32.right = t43

print(Solution().pathSum(t1, 8))
