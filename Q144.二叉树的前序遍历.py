#!/usr/bin/env python3

# https://leetcode-cn.com/problems/binary-tree-preorder-traversal
# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 输出: [1,2,3]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> [int]:
        res = list()
        treeList = [root]
        while len(treeList) > 0:
            node = treeList.pop()
            if node:
                res.append(node.val)
                treeList.append(node.right)
                treeList.append(node.left)
        return res


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.right = t2
t2.left = t3
print(Solution().preorderTraversal(t1))
