#!/usr/bin/env python3

# https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。
# 如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。 
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
#
# 示例 1:
# 输入:
#     2
#    / \
#   2   5
#      / \
#     5   7
# 输出: 5
# 说明: 最小的值是 2 ，第二小的值是 5 。
#
# 示例 2:
# 输入:
#     2
#    / \
#   2   2
# 输出: -1
# 说明: 最小的值是 2, 但是不存在第二小的值。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = list()

        def coverTree(r: TreeNode):
            if r is not None:
                res.append(r.val)
                if (len(res) > 1 and res[0] == res[-1]) or (len(res) > 2 and res[1] == res[-1]):
                    res.pop(-1)
                if len(res) > 1 and res[0] > res[-1]:
                    res[0], res[-1] = res[-1], res[0]
                if len(res) > 2 and res[1] > res[-1]:
                    res[1], res[-1] = res[-1], res[1]
                coverTree(r.left)
                coverTree(r.right)

        coverTree(root)
        if len(res) <= 1:
            return -1
        else:
            return res[1]


t1 = TreeNode(5)
t2 = TreeNode(5)
t3 = TreeNode(8)
t1.left = t2
t1.right = t3
print(Solution().findSecondMinimumValue(t1))
