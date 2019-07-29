#!/usr/bin/env python3

# 删除链表中等于给定值 val 的所有节点。
#
# 示例:
#
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        result = None
        preNode = None
        while head is not None:
            if head.val != val:
                if preNode is None:
                    preNode = ListNode(head.val)
                    result = preNode
                else:
                    preNode.next = ListNode(head.val)
                    preNode = preNode.next
            head = head.next
        return result


l0 = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(6)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l0.next = l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

res = Solution().removeElements(l0, 6)
while res is not None:
    print(res.val)
    res = res.next
