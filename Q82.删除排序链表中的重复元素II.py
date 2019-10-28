#!/usr/bin/env python3

# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#
# 示例 2:
# 输入: 1->1->1->2->3
# 输出: 2->3


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = None
        while head is not None:
            nextV = head.next
            flag = False
            # 去掉开始的
            while nextV is not None and nextV.val == head.val:
                head = nextV
                nextV = nextV.next
                flag = True
            if flag:
                head = nextV
                continue

            # 去掉后俩
            flag = False
            next2V = None if nextV is None else nextV.next
            while nextV is not None and next2V is not None and nextV.val == next2V.val:
                flag = True
                nextV = next2V
                next2V = next2V.next

            if flag:
                head.next = next2V
                continue

            if res is None:
                res = head
            head = head.next
        return res


l1 = ListNode(1)
l2 = ListNode(1)
l1.next = l2
l3 = ListNode(1)
l2.next = l3
l4 = ListNode(1)
l3.next = l4
l5 = ListNode(3)
l4.next = l5
l6 = ListNode(4)
l5.next = l6
l7 = ListNode(4)
l6.next = l7
l8 = ListNode(5)
l7.next = l8
l9 = ListNode(5)
l8.next = l9


l0 = Solution().deleteDuplicates(l1)
while l0 is not None:
    print(l0.val)
    l0 = l0.next
