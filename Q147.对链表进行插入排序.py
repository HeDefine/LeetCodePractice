#!/usr/bin/env python3

# https://leetcode-cn.com/problems/insertion-sort-list
# 对链表进行插入排序。
# 从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
#
# 插入排序算法：
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
#
# 示例 1：
# 输入: 4->2->1->3
# 输出: 1->2->3->4
#
# 示例 2：
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        def insert(root: ListNode, newNode: ListNode) -> ListNode:
            tempHead = root
            lastNode = None
            while root is not None and newNode is not None:
                if newNode.val < root.val:
                    newNode.next = root
                    if lastNode is not None:
                        lastNode.next = newNode
                    else:
                        tempHead = newNode
                    newNode = None
                lastNode = root
                root = root.next
            if newNode is not None:
                if lastNode is not None:
                    lastNode.next = newNode
                else:
                    tempHead = newNode
            return tempHead

        res = None
        while head is not None:
            nextNode = head.next
            head.next = None
            res = insert(res, head)

            head = nextNode
        return res


l1 = ListNode(4)
l2 = ListNode(2)
l3 = ListNode(1)
l4 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l4
l0 = Solution().insertionSortList(l1)
while l0 is not None:
    print(l0.val)
    l0 = l0.next
print('-----------------')
n1 = ListNode(-1)
n2 = ListNode(5)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(0)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n0 = Solution().insertionSortList(n1)
while n0 is not None:
    print(n0.val)
    n0 = n0.next
