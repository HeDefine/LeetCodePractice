# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例 1：
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#
# 示例 2：
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
# 示例 3：
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def recursion(node:ListNode) -> int:
            if node is None:
                return 0
            return recursion(node.next) * 10 + node.val
        sum_val = recursion(l1) + recursion(l2)
        
        temp = ListNode(0)
        first = temp
        while sum_val > 0:
            temp.val = sum_val % 10
            sum_val = sum_val // 10
            if sum_val > 0:
                temp.next = ListNode(0)
                temp = temp.next
        return first
        

l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(3)
l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)
l2_1.next = l2_2
l2_2.next = l2_3

print(Solution().addTwoNumbers(l1_1, l2_1))

print(Solution().addTwoNumbers(ListNode(0), ListNode(0)))
