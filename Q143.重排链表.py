#!/usr/bin/env python3

# https://leetcode-cn.com/problems/reorder-list
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
# 示例 2:
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        temp = list()
        while head is not None:
            temp.append(head)
            head = head.next
        flag = True
        last = None
        while len(temp) > 0:
            node = temp.pop(0 if flag else -1)
            node.next = None
            if last:
                last.next = node
            last = node
            flag = not flag


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
Solution().reorderList(l1)
while l1 is not None:
    print(l1.val)
    l1 = l1.next
