#!/usr/bin/env python3

# https://leetcode-cn.com/problems/leaf-similar-trees
# 请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
#
# 举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
# 如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
# 如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
#
# 提示：
# 给定的两颗树可能会有 1 到 100 个结点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def coverTree(t: TreeNode) -> [int]:
            if t is None:
                return []
            res = list()
            if t.left is None and t.right is None:
                res = [t.val]
            if t.left is not None:
                res = res + coverTree(t.left)
            if t.right is not None:
                res = res + coverTree(t.right)
            return res
        return coverTree(root1) == coverTree(root2)


t1 = TreeNode(3)
t2 = TreeNode(5)
t3 = TreeNode(1)
t1.left = t2
t1.right = t3
t4 = TreeNode(6)
t5 = TreeNode(2)
t6 = TreeNode(9)
t7 = TreeNode(8)
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
t8 = TreeNode(7)
t9 = TreeNode(4)
t5.left = t8
t5.right = t9

print(Solution().leafSimilar(t1, t2))
