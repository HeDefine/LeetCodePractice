#!/usr/bin/env python3

# https://leetcode-cn.com/problems/swap-nodes-in-pairs
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例:
# 给定 1->2->3->4, 你应该返回 2->1->4->3.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is not None:
            front = head
            back = head.next
            if back is not None:
                nextL = self.swapPairs(back.next)
                front.next = nextL
                back.next = front
                return back
            else:
                return front


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4

l = Solution().swapPairs(l1)
while l is not None:
    print(l.val)
    l = l.next
