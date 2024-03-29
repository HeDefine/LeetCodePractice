#!/usr/bin/env python3

# https://leetcode-cn.com/problems/quad-tree-intersection
# 四叉树是一种树数据，其中每个结点恰好有四个子结点：topLeft、topRight、bottomLeft 和 bottomRight。四叉树通常被用来划分一个二维空间，递归地将其细分为四个象限或区域。
# 我们希望在四叉树中存储 True/False 信息。四叉树用来表示 N * N 的布尔网格。
# 对于每个结点, 它将被等分成四个孩子结点直到这个区域内的值都是相同的。
# 每个节点都有另外两个布尔属性：isLeaf 和 val。
# 当这个节点是一个叶子结点时 isLeaf 为真。
# val 变量储存叶子结点所代表的区域的值。
#
# 例如，下面是两个四叉树 A 和 B：
# A:
# +-------+-------+   T: true
# |       |       |   F: false
# |   T   |   T   |
# |       |       |
# +-------+-------+
# |       |       |
# |   F   |   F   |
# |       |       |
# +-------+-------+
# topLeft: T
# topRight: T
# bottomLeft: F
# bottomRight: F
#
# B:
# +-------+---+---+
# |       | F | F |
# |   T   +---+---+
# |       | T | T |
# +-------+---+---+
# |       |       |
# |   T   |   F   |
# |       |       |
# +-------+-------+
# topLeft: T
# topRight:
#      topLeft: F
#      topRight: F
#      bottomLeft: T
#      bottomRight: T
# bottomLeft: T
# bottomRight: F
#
# 你的任务是实现一个函数，该函数根据两个四叉树返回表示这两个四叉树的逻辑或(或并)的四叉树。
# A:                 B:                 C (A or B):
# +-------+-------+  +-------+---+---+  +-------+-------+
# |       |       |  |       | F | F |  |       |       |
# |   T   |   T   |  |   T   +---+---+  |   T   |   T   |
# |       |       |  |       | T | T |  |       |       |
# +-------+-------+  +-------+---+---+  +-------+-------+
# |       |       |  |       |       |  |       |       |
# |   F   |   F   |  |   T   |   F   |  |   T   |   F   |
# |       |       |  |       |       |  |       |       |
# +-------+-------+  +-------+-------+  +-------+-------+
#  
# 提示：
# A 和 B 都表示大小为 N * N 的网格。
# N 将确保是 2 的整次幂。
# 如果你想了解更多关于四叉树的知识，你可以参考这个 wiki 页面。
# 逻辑或的定义如下：如果 A 为 True ，或者 B 为 True ，或者 A 和 B 都为 True，则 "A 或 B" 为 True。


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: Node, quadTree2: Node) -> Node:
        if (quadTree1.isLeaf and quadTree1.val) or (quadTree2.isLeaf and not quadTree2.val):
            return quadTree1
        elif (quadTree2.isLeaf and quadTree2.val) or (quadTree1.isLeaf and not quadTree1.val):
            return quadTree2
        else:
            res = Node(False, False, None, None, None, None)
            res.topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            res.topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            res.bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            res.bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            if res.topLeft.isLeaf \
                    & res.topRight.isLeaf \
                    & res.bottomLeft.isLeaf\
                    & res.bottomRight.isLeaf\
                    & res.topLeft.val == res.topRight.val\
                    & res.topRight.val == res.bottomLeft.val\
                    & res.bottomLeft.val == res.bottomRight.val:
                res = res.topLeft
            return res
