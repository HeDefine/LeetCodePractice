#!/usr/bin/env python3

# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal
# 给定一个 N 叉树，返回其节点值的前序遍历。
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> [int]:
        if root is None:
            return []
        li = [root.val]
        for r in root.children:
            li += self.preorder(r)
        return li

