#!/usr/bin/env python3

# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
# 说明：
# 给定的 n 保证是有效的。
#
# 进阶：
# 你能尝试使用一趟扫描实现吗？


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = list()
        while head is not None:
            temp.append(head)
            head = head.next

        l0 = temp.pop(-n)
        if -n >= -len(temp):
            temp[-n].next = l0.next
        return temp[0] if len(temp) > 0 else None


l1 = ListNode(1)
# l2 = ListNode(2)
# l1.next = l2
# l3 = ListNode(3)
# l2.next = l3
# l4 = ListNode(4)
# l3.next = l4
# l5 = ListNode(5)
# l4.next = l5
l = Solution().removeNthFromEnd(l1, 1)
while l is not None:
    print(l.val)
    l = l.next
