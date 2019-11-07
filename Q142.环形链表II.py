#!/usr/bin/env python3

# https://leetcode-cn.com/problems/linked-list-cycle-ii
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 说明：不允许修改给定的链表。
#
# 进阶：
# 你是否可以不用额外空间解决此题？


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        quick = head
        if slow is not None and quick is not None and quick.next is not None:
            slow = slow.next
            quick = quick.next.next
        else:
            return None

        while slow != quick:
            if slow is not None and quick is not None and quick.next is not None:
                slow = slow.next
                quick = quick.next.next
            else:
                return None

        while head != slow:
            head = head.next
            slow = slow.next
        return head


n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)
temp1 = ListNode(11)
temp2 = ListNode(22)
temp3 = ListNode(33)
temp4 = ListNode(44)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = temp1
temp1.next = temp2
temp2.next = temp3
temp3.next = temp4
temp4.next = n2
# n4.next = n2

n0 = Solution().detectCycle(n1)
print(n0.val)  # 2

# l1 = ListNode(1)
# l2 = ListNode(2)
# l1.next = l2
# l2.next = l1
# l0 = Solution().detectCycle(l1)
# print(l1.val)  # 1
#
# t1 = ListNode(1)
# t0 = Solution().detectCycle(t1)
# print(t0.val if t0 else -1)  # None
