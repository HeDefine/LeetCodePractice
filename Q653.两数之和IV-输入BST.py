#!/usr/bin/env python3

# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst
# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
#
# 案例 1:
# 输入:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# Target = 9
# 输出: True
#  
# 案例 2:
# 输入:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# Target = 28
# 输出: False


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def coverTree(r: TreeNode):
            if r is None:
                return
            res[r.val] = res.get(r.val, 0) + 1
            coverTree(r.left)
            coverTree(r.right)

        res = dict()
        coverTree(root)
        for i in res.keys():
            if res.get(k - i) is not None:
                if i != k - i or (i == k - i and res[i] > 1):
                    return True
        return False


t1 = TreeNode(5)
t2 = TreeNode(3)
t3 = TreeNode(6)
t4 = TreeNode(2)
t5 = TreeNode(4)
t6 = TreeNode(7)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.right = t6
# print(Solution().findTarget(t1, 9))  # True
# print(Solution().findTarget(t1, 28))  # False

n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
print(Solution().findTarget(n1, 4))
