#!/usr/bin/env python3

# https://leetcode-cn.com/problems/binary-search-tree-iterator
# 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
# 调用 next() 将返回二叉搜索树中的下一个最小的数。
#
#  
# 提示：
# next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.treeList = list()
        temp = list()
        while root is not None or len(temp) > 0:
            while root is not None:
                temp.append(root)
                root = root.left
            root = temp.pop()
            self.treeList.append(root)
            root = root.right
        self.idx = 0

    def next(self) -> int:
        if self.idx < len(self.treeList):
            res = self.treeList[self.idx].val
            self.idx += 1
            return res

    def hasNext(self) -> bool:
        return self.idx < len(self.treeList)


t1 = TreeNode(7)
t2 = TreeNode(3)
t3 = TreeNode(15)
t4 = TreeNode(9)
t5 = TreeNode(20)
t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5

iterator = BSTIterator(t1)
print(iterator.next())  # 返回 3
print(iterator.next())  # 返回 7
print(iterator.hasNext())  # 返回 true
print(iterator.next())  # 返回 9
print(iterator.hasNext())  # 返回 true
print(iterator.next())  # 返回 15
print(iterator.hasNext())  # 返回 true
print(iterator.next())  # 返回 20
print(iterator.hasNext())  # 返回 false
