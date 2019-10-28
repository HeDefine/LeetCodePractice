#!/usr/bin/env python3

# https://leetcode-cn.com/problems/partition-list
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        node1Head = None
        node1Foot = None
        node2Head = None
        node2Foot = None
        while head is not None:
            if head.val < x:
                if node1Foot is None:
                    node1Foot = ListNode(head.val)
                    node1Head = node1Foot
                else:
                    node1Foot.next = ListNode(head.val)
                    node1Foot = node1Foot.next
            else:
                if node2Foot is None:
                    node2Foot = ListNode(head.val)
                    node2Head = node2Foot
                else:
                    node2Foot.next = ListNode(head.val)
                    node2Foot = node2Foot.next
            head = head.next

        if node1Foot is not None:
            node1Foot.next = node2Head
        else:
            return node2Head
        return node1Head


l1 = ListNode(1)
l2 = ListNode(4)
l3 = ListNode(3)
l4 = ListNode(2)
l5 = ListNode(5)
l6 = ListNode(2)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

l0 = Solution().partition(l1, 3)
while l0 is not None:
    print(l0.val)
    l0 = l0.next
