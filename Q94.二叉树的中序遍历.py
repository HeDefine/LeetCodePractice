#!/usr/bin/env python3

# https://leetcode-cn.com/problems/binary-tree-inorder-traversal
# 给定一个二叉树，返回它的中序 遍历。
# 示例:
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        res = list()
        stack = list()
        while root is not None or len(stack) > 0:
            while root is not None:
                if root is not None:
                    stack.append(root)
                    root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.right = t2
t2.left = t3

print(Solution().inorderTraversal(t1))
