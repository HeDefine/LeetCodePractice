#!/usr/bin/env python3

# https://leetcode-cn.com/problems/merge-two-sorted-lists
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        temp = result
        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    minValue = l1.val
                    l1 = l1.next
                else:
                    minValue = l2.val
                    l2 = l2.next
            elif l1 is not None:
                minValue = l1.val
                l1 = l1.next
            else:
                minValue = l2.val
                l2 = l2.next
            temp.next = ListNode(minValue)
            temp = temp.next
        return result.next


l01 = ListNode(1)
l02 = ListNode(2)
l03 = ListNode(4)
l01.next = l02
l02.next = l03

l11 = ListNode(1)
l12 = ListNode(3)
l13 = ListNode(4)
l11.next = l12
l12.next = l13

ln = Solution().mergeTwoLists(l01, l11)
s = ""
if ln is not None and ln.val is not None:
    s = s + str(ln.val)
while ln is not None and ln.next is not None:
    ln = ln.next
    s = s + "->" + str(ln.val)

print(s)

# 解题思路: 一个个遍历。没啥好说的
