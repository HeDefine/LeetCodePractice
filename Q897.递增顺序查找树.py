#!/usr/bin/env python3

# https://leetcode-cn.com/problems/increasing-order-search-tree
# 给定一个树，按中序遍历重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。
#
# 示例 ：
# 输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]
#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
#  /        / \
# 1        7   9
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#  1
#   \
#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6
#             \
#              7
#               \
#                8
#                 \
#                  9
# 提示：
# 1. 给定树中的结点数介于 1 和 100 之间。
# 2. 每个结点都有一个从 0 到 1000 范围内的唯一整数值。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def coverTree(t: TreeNode):
            if t is None:
                return []
            return coverTree(t.left) + [t.val] + coverTree(t.right)
        temp = coverTree(root)
        head = None
        tree = None
        for i in temp:
            if tree is None:
                tree = TreeNode(i)
                head = tree
            else:
                tree.right = TreeNode(i)
                tree = tree.right
        return head


t1 = TreeNode(5)
t2 = TreeNode(3)
t3 = TreeNode(6)
t1.left = t2
t1.right = t3

t4 = TreeNode(2)
t5 = TreeNode(4)
t6 = TreeNode(8)
t2.left = t4
t2.right = t5
t3.right = t6

t7 = TreeNode(1)
t8 = TreeNode(7)
t9 = TreeNode(9)
t4.left = t7
t6.left = t8
t6.right = t9

result = Solution().increasingBST(t1)


def cover(r: TreeNode):
    if r is None:
        return ['null']
    return [r.val] + cover(r.left) + cover(r.right)


print(cover(result))  # [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
