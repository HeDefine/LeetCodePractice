#!/usr/bin/env python3

# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
#
# 例如，给定一个 3叉树 :
# 返回其层序遍历:
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#
# 说明:
#
# 树的深度不会超过 1000。
# 树的节点总数不会超过 5000。

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> [[int]]:
        def reviewLevel(r: Node, t: [[int]], lev: int):
            if len(t) <= lev:
                t.append([r.val])
            else:
                t[lev].append(r.val)

            if r.children is not None:
                for n in r.children:
                    reviewLevel(n, t, lev + 1)

        if root is not None:
            result = list()
            reviewLevel(root, result, 0)
            return result
        else:
            return None


t1 = Node(1, [Node(3, [Node(5, None), Node(6, None)]), Node(2, None), Node(4, None)])

print(Solution().levelOrder(t1))
