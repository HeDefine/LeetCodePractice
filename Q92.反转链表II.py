#!/usr/bin/env python3

# https://leetcode-cn.com/problems/reverse-linked-list-ii
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        idx = 0
        pre = head
        splitFoot = None

        newHead = None
        newFoot = None
        while head is not None:
            idx += 1
            if idx == m - 1:
                splitFoot = head
            elif idx == m:
                newHead = ListNode(head.val)
                newFoot = newHead
                newFoot.next = head.next
            elif m < idx <= n:
                temp = ListNode(head.val)
                temp.next = newHead
                newHead = temp
                newFoot.next = head.next
            head = head.next
        if splitFoot is not None:
            splitFoot.next = newHead
        else:
            pre = newHead
        return pre


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

l0 = Solution().reverseBetween(l4, 1, 2)
while l0 is not None:
    print(l0.val)
    l0 = l0.next
