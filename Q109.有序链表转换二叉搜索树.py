#!/usr/bin/env python3

# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
# 给定的有序链表： [-10, -3, 0, 5, 9],
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        def recursion(l: [int]) -> TreeNode:
            res = None
            if len(l) > 0:
                mid = len(l) // 2
                val = l[mid]
                res = TreeNode(val)
                res.left = recursion(l[:mid])
                res.right = recursion(l[mid + 1:])
            return res

        temp = list()
        while head is not None:
            temp.append(head.val)
            head = head.next
        return recursion(temp)


t1 = ListNode(-10)
t2 = ListNode(-3)
t3 = ListNode(0)
t4 = ListNode(5)
t5 = ListNode(9)
t1.next = t2
t2.next = t3
t3.next = t4
t4.next = t5

t = Solution().sortedListToBST(t1)
print(t.val)