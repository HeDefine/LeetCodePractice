#!/usr/bin/env python3

# https://leetcode-cn.com/problems/same-tree
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
# 示例 1:
# 输入:       1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# 输出: true
#
# 示例 2:
# 输入:      1          1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# 输出: false
#
# 示例 3:
# 输入:       1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# 输出: false


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)
            else:
                return False
        elif p is None and q is None:
            return True
        else:
            return False


tree10 = TreeNode(1)
tree11 = TreeNode(2)
tree12 = TreeNode(3)
tree10.left = tree11
tree10.right = tree12

tree20 = TreeNode(1)
tree21 = TreeNode(2)
tree22 = TreeNode(3)
tree20.left = tree21
tree20.right = tree22

print(Solution().isSameTree(tree10, tree20))


# 题解: 用递归的方式。一遍遍遍历下去.DLR遍历