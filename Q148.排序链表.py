#!/usr/bin/env python3

# https://leetcode-cn.com/problems/sort-list
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1:
# 输入: 4->2->1->3
# 输出: 1->2->3->4
#
# 示例 2:
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        length = 0
        tempHead = head
        while tempHead is not None:
            tempHead = tempHead.next
            length += 1
        # [4, 2, 1, 3, 5]
        space = 1
        while space < length:
            stepHeadNode = None
            stepLastNode = None
            tempHead = head
            while tempHead is not None:
                h1, f1 = tempHead, tempHead
                for i in range(space):
                    if tempHead:
                        f1 = tempHead
                        tempHead = tempHead.next
                f1.next = None
                if tempHead is None:
                    stepLastNode.next = h1
                    break
                h2, f2 = tempHead, tempHead
                for i in range(space):
                    if tempHead:
                        f2 = tempHead
                        tempHead = tempHead.next
                f2.next = None

                while h1 is not None or h2 is not None:
                    curNode = None
                    if h2 is None or (h1 and h2 and h1.val < h2.val):
                        curNode = h1
                        h1 = h1.next
                    else:
                        curNode = h2
                        h2 = h2.next

                    curNode.next = None
                    if stepLastNode is not None:
                        stepLastNode.next = curNode
                        stepLastNode = stepLastNode.next

                    if stepHeadNode is None:
                        stepHeadNode = curNode
                        stepLastNode = curNode
            head = stepHeadNode
            space *= 2
        return head


l1 = ListNode(4)
l2 = ListNode(2)
l3 = ListNode(1)
l4 = ListNode(3)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l0 = Solution().sortList(l1)
while l0 is not None:
    print(l0.val)
    l0 = l0.next
