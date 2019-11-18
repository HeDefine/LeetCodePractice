#!/usr/bin/env python3

# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
#
# 示例 1:
# 输入: root = [3,1,4,null,2], k = 1
# 输出: 1
#
# 示例 2:
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
# 输出: 3
# 进阶：
# 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        flag = 0
        treeStack = list()
        while root is not None or len(treeStack) > 0:
            while root is not None:
                treeStack.append(root)
                root = root.left
            t = treeStack.pop()
            flag += 1
            if flag == k:
                return t.val
            root = t.right
        return 0


n1 = TreeNode(3)
n2 = TreeNode(1)
n3 = TreeNode(4)
n4 = TreeNode(2)
n1.left = n2
n1.right = n3
n2.right = n4
print(Solution().kthSmallest(n1, 1))  # 1

t1 = TreeNode(5)
t2 = TreeNode(3)
t3 = TreeNode(6)
t1.left = t2
t1.right = t3
t4 = TreeNode(2)
t5 = TreeNode(4)
t2.left = t4
t2.right = t5
t6 = TreeNode(1)
t4.left = t6
print(Solution().kthSmallest(t1, 3))  # 3
