#!/usr/bin/env python3

# 链接：https://leetcode-cn.com/problems/symmetric-tree
# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#     1
#    / \
#   2   2
#    \   \
#    3    3


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirrorTree(root, root)

    def isMirrorTree(self, t1: TreeNode, t2: TreeNode):
        if t1 is None and t2 is None:
            return True
        elif t1 is not None and t2 is not None:
            if t1.val == t2.val:
                return self.isMirrorTree(t1.left, t2.right) \
                       & self.isMirrorTree(t1.right, t2.left)
            else:
                return False
        else:
            return False


t01 = TreeNode(1)
t02 = TreeNode(2)
t03 = TreeNode(2)
t04 = TreeNode(3)
t05 = TreeNode(4)
t06 = TreeNode(4)
t07 = TreeNode(3)

t01.left = t02
t01.right = t03
t02.left = t04
t02.right = t05
t03.left = t06
t03.right = t07

print(Solution().isSymmetric(t01))


# 题解: 这题的难点主要是 怎么判定一个树是对称二叉树
# 1. 根的值相同
# 2. 每棵树左边对称另一棵树的右边
