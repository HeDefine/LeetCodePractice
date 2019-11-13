#!/usr/bin/env python3

# https://leetcode-cn.com/problems/binary-tree-right-side-view
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例:
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        def recursion(level, r: TreeNode):
            if r is not None:
                if level >= len(temp):
                    temp.append(r.val)
                else:
                    temp[level] = r.val
                recursion(level + 1, r.left)
                recursion(level + 1, r.right)

        temp = list()
        recursion(0, root)
        return temp


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t2.right = t5
t3.right = t4
print(Solution().rightSideView(t1))
