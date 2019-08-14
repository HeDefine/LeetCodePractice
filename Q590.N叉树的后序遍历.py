#!/usr/bin/env python3

# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal
# 给定一个 N 叉树，返回其节点值的后序遍历。
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> [int]:
        if root is None:
            return []
        li = list()
        for r in root.children:
            li += self.postorder(r)
        li += [root.val]
        return li



