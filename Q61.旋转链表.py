#!/usr/bin/env python3

# https://leetcode-cn.com/problems/rotate-list
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#
# 示例 2:
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = 1
        pre = head
        while head is not None:
            if head.next is None:
                head.next = pre
                head = head.next
                break
            length += 1
            head = head.next
        k = length - k % length
        idx = 0
        last = None
        while head is not None:
            if idx == k - 1:
                last = head
            elif idx == k:
                last.next = None
                break
            head = head.next
            idx += 1

        return head


l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
l3 = ListNode(3)
l2.next = l3
l4 = ListNode(4)
l3.next = l4
l5 = ListNode(5)
l4.next = l5

l0 = Solution().rotateRight(l1, 2)
while l0 is not None:
    print(l0.val)
    l0 = l0.next
