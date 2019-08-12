#!/usr/bin/env python3

# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst
# 给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。
#
# 示例 :
# 输入:
#    1
#     \
#      3
#     /
#    2
# 输出:
# 1
#
# 解释:
# 最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def getTreeValue(r: TreeNode) -> [int]:
            if r is None:
                return []
            return getTreeValue(r.left) + [r.val] + getTreeValue(r.right)
        res = getTreeValue(root)
        if root is not None:
            minV = res[-1]
            for idx, v in enumerate(res):
                minV = min(minV, abs(v - res[idx - 1]))
            return minV
        return 0


T0 = TreeNode(1)
T1 = TreeNode(5)
T2 = TreeNode(3)
T0.right = T1
T1.left = T2
print(Solution().getMinimumDifference(T0))
