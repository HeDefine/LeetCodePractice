#!/usr/bin/env python3

# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 返回其自底向上的层次遍历为：
# [
#   [15,7],
#   [9,20],
#   [3]
# ]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        if root is None:
            return None

        currentStepTrees = [root]
        newStepTrees = list()

        result = list()
        idx = 0
        while len(currentStepTrees) > 0:
            currentTree = currentStepTrees.pop(0)
            if len(result) <= idx:
                result.append([currentTree.val])
            else:
                result[idx].append(currentTree.val)

            if currentTree.left is not None:
                newStepTrees.append(currentTree.left)

            if currentTree.right is not None:
                newStepTrees.append(currentTree.right)

            if len(currentStepTrees) == 0 and len(newStepTrees) > 0:
                # 开始放到下一列
                currentStepTrees.extend(newStepTrees)
                newStepTrees.clear()
                idx += 1
        result.reverse()
        return result


t0 = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
t3 = TreeNode(15)
t4 = TreeNode(7)

t0.left = t1
t0.right = t2
t2.left = t3
t2.right = t4

print(Solution().levelOrderBottom(t0))

# 题解. 二叉树的层序遍历。利用队列的先进先出
