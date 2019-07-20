#!/usr/bin/env python3

# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
# 输入: 1->1->2
# 输出: 1->2
#
# 示例 2:
# 输入: 1->1->2->3->3
# 输出: 1->2->3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        result = ListNode(head.val)
        temp = result
        while head.next is not None:
            nextV = head.next
            if nextV.val != temp.val:
                temp.next = ListNode(nextV.val)
                temp = temp.next
            head = head.next
        return result


l10 = ListNode(1)
l11 = ListNode(1)
l12 = ListNode(2)
l10.next = l11
l11.next = l12

r1 = Solution().deleteDuplicates(l10)
while r1 is not None:
    print(r1.val)
    r1 = r1.next

