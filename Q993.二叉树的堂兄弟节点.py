#!/usr/bin/env python3

# https://leetcode-cn.com/problems/cousins-in-binary-tree
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
# 如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
# 我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。
#
# 示例 1：
# 输入：root = [1,2,3,4], x = 4, y = 3
# 输出：false
#
# 示例 2：
# 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
# 输出：true
#
# 示例 3：
# 输入：root = [1,2,3,null,4], x = 2, y = 3
# 输出：false
#
# 提示：
# 二叉树的节点数介于 2 到 100 之间。
# 每个节点的值都是唯一的、范围为 1 到 100 的整数。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def coverTree(t: TreeNode, depth: int):
            if t is not None:
                if t.val == x:
                    depthXY[0] = depth
                if t.val == y:
                    depthXY[1] = depth
                if t.left is not None and t.right is not None:
                    if (t.left.val == x and t.right.val == y) or (t.left.val == y and t.right.val == x):
                        return
                coverTree(t.left, depth + 1)
                coverTree(t.right, depth + 1)

        depthXY = [-1, -1]
        coverTree(root, 0)
        return depthXY[0] == depthXY[1] and depthXY != [-1, -1]


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t2.left = t4
t3.right = t5
t3.left = TreeNode(6)

print(Solution().isCousins(t1, 5, 4))  # True
print(Solution().isCousins(t1, 4, 3))  # False
print(Solution().isCousins(t1, 2, 3))  # False
print(Solution().isCousins(t1, 5, 6))  # False
