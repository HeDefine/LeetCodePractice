#!/usr/bin/env python3

# https://leetcode-cn.com/problems/reverse-linked-list
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preNode = None
        curNode = head
        while curNode is not None:
            temp = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = temp
        return preNode





l0 = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(3)
l3 = ListNode(4)
l4 = ListNode(5)
l0.next = l1
l1.next = l2
l2.next = l3
l3.next = l4

result = Solution().reverseList(l0)
while result is not None:
    print(result.val)
    result = result.next
