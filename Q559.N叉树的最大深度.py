#!/usr/bin/env python3

# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree
# 给定一个 N 叉树，找到其最大深度。
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# 说明:
# 树的深度不会超过 1000。
# 树的节点总不会超过 5000。


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        if root is None:
            return 0
        if root.children is None:
            return 1
        else:
            maxV = 0
            for n in root.children:
                maxV = max(maxV, self.maxDepth(n)) + 1
            return maxV
