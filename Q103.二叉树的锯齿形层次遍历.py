#!/usr/bin/env python3

# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        def cover(lever: int, r: TreeNode):
            if r is not None:
                if lever < len(res):
                    if lever % 2 == 0:
                        res[lever].append(r.val)
                    else:
                        res[lever] = [r.val] + res[lever]
                else:
                    res.append([r.val])
                cover(lever + 1, r.left)
                cover(lever + 1, r.right)

        res = list()
        cover(0, root)
        return res


t1 = TreeNode(3)
t2 = TreeNode(9)
t3 = TreeNode(20)
t4 = TreeNode(15)
t5 = TreeNode(7)
t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5
print(Solution().zigzagLevelOrder(t1))
