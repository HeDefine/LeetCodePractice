#!/usr/bin/env python3

# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes
# 给定一个二叉搜索树的根结点 root, 返回树中任意两节点的差的最小值。
#
# 示例：
# 输入: root = [4,2,6,1,3,null,null]
# 输出: 1
# 解释:
# 注意，root是树结点对象(TreeNode object)，而不是数组。
# 给定的树 [4,2,6,1,3,null,null] 可表示为下图:
#           4
#         /   \
#       2      6
#      / \
#     1   3
# 最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
#
# 注意：
# 二叉树的大小范围在 2 到 100。
# 二叉树总是有效的，每个节点的值都是整数，且不重复。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def LDRCoverTree(r: TreeNode) -> [int]:
            if r is None:
                return []
            return LDRCoverTree(r.left) + [r.val] + LDRCoverTree(r.right)

        allVal = LDRCoverTree(root)
        res = 100
        for i in range(len(allVal) - 1):
            res = min(res, abs(allVal[i] - allVal[i + 1]))
        return res


T0 = TreeNode(4)
T1 = TreeNode(2)
T2 = TreeNode(6)
T3 = TreeNode(1)
T4 = TreeNode(3)
T0.left = T1
T0.right = T2
T1.left = T3
T1.right = T4

print(Solution().minDiffInBST(T0))  # 1
