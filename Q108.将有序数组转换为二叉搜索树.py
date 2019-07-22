#!/usr/bin/env python3

# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
# 给定有序数组: [-10,-3,0,5,9],
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        if nums is None:
            return TreeNode(None)

        midIdx = len(nums) // 2
        print(midIdx)
        result = TreeNode(nums[midIdx])

        if midIdx > 0:
            result.left = self.sortedArrayToBST(nums[:midIdx])

        if midIdx + 1 < len(nums):
            result.right = self.sortedArrayToBST(nums[midIdx + 1:])

        return result


print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))

# 题解:
# WIKI 百科:
# 二叉查找树（Binary Search Tree）（又：二叉搜索树，二叉排序树）
# 它或者是一棵空树，或者是具有下列性质的二叉树：
# 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
# 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
# 它的左、右子树也分别为二叉排序树。
#
# 所以每次都找中位数填充就可以了

