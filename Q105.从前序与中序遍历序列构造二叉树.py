#!/usr/bin/env python3

# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# 根据一棵树的前序遍历与中序遍历构造二叉树。
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        res = None
        if len(preorder) > 0:
            curVal = preorder[0]
            for idx, val in enumerate(inorder):
                if val == curVal:
                    preorder.pop(0)
                    res = TreeNode(curVal)
                    res.left = self.buildTree(preorder, inorder[:idx])
                    res.right = self.buildTree(preorder, inorder[idx + 1:])

        return res


t0 = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(t0)
