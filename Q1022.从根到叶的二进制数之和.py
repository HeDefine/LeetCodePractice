#!/usr/bin/env python3

# https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers
# 给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。
# 例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。
# 对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
# 以 10^9 + 7 为模，返回这些数字之和。
#
# 示例：
# 输入：[1,0,1,0,1,0,1]
# 输出：22
# 解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
#
# 提示：
# 1. 树中的结点数介于 1 和 1000 之间。
# 2. node.val 为 0 或 1 。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def coverTree(t: TreeNode, cur: str):
            if t is not None:
                if t.left is None and t.right is None:
                    res.append(cur + str(t.val))
                else:
                    if t.left is not None:
                        coverTree(t.left, cur + str(t.val))
                    if t.right is not None:
                        coverTree(t.right, cur + str(t.val))

        res = list()
        coverTree(root, '')
        return sum([int(val, 2) for val in res])


t0 = TreeNode(1)
t1 = TreeNode(0)
t2 = TreeNode(1)
t3 = TreeNode(0)
t4 = TreeNode(1)
t5 = TreeNode(0)
t6 = TreeNode(1)
t0.left = t1
t0.right = t2
t1.left = t3
t1.right = t4
t2.left = t5
t2.right = t6
print(Solution().sumRootToLeaf(t0))
