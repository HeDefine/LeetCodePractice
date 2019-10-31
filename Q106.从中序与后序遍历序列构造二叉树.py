#!/usr/bin/env python3

# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:
        res = None
        if len(postorder) > 0:
            curVal = postorder[-1]
            for idx, val in enumerate(inorder):
                if val == curVal:
                    postorder.pop()
                    res = TreeNode(curVal)
                    res.right = self.buildTree(inorder[idx + 1:], postorder)
                    res.left = self.buildTree(inorder[:idx], postorder)

        return res


t0 = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
print(t0)
