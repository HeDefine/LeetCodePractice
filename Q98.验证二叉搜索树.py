#!/usr/bin/env python3

# https://leetcode-cn.com/problems/validate-binary-search-tree
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 假设一个二叉搜索树具有如下特征：
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
# 示例 1:
# 输入:
#     2
#    / \
#   1   3
# 输出: true
#
# 示例 2:
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = list()
        pre = None
        while root is not None or len(stack) > 0:
            while root is not None:
                stack.append(root)
                root = root.left
            curTree = stack.pop()
            if pre is not None and curTree.val <= pre.val:
                return False
            pre = curTree
            root = curTree.right
        return True


t1 = TreeNode(2)
t2 = TreeNode(1)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
print(Solution().isValidBST(t1))  # True

t1 = TreeNode(5)
t2 = TreeNode(1)
t3 = TreeNode(4)
t4 = TreeNode(3)
t5 = TreeNode(6)
t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5
print(Solution().isValidBST(t1))  # False

#     10
#    / \
#  5    15
#       / \
#      6  20

t1 = TreeNode(10)
t2 = TreeNode(5)
t3 = TreeNode(15)
t4 = None
t5 = None
t6 = TreeNode(6)
t7 = TreeNode(20)
t1.left = t2
t1.right = t3
t2.left = None
t2.right = None
t3.left = t6
t3.right = t7
print(Solution().isValidBST(t1))  # False
