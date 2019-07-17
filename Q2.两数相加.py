#!/usr/bin/env python3

# https://leetcode-cn.com/problems/add-two-numbers/
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 方法1: 把l1,l2变成两个实数，然后相加后的值，再变成链表. 3次循环
    @staticmethod
    def addTwoNumbers1(l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)

        val1 = 0
        temp = l1
        i = 0
        while temp is not None:
            val1 += temp.val * pow(10, i)
            temp = temp.next
            i += 1

        val2 = 0
        temp = l2
        i = 0
        while temp is not None:
            val2 += temp.val * pow(10, i)
            temp = temp.next
            i += 1
        print(val1, val2)

        val0 = val1 + val2
        print(val0)

        temp = result
        while val0 > 0:
            temp.val = val0 % 10
            val0 = val0 // 10
            if val0 > 0:
                temp.next = ListNode(0)
                temp = temp.next
        return result

    # 对上述方法进行优化, 集成到一个
    @staticmethod
    def addTwoNumbers2(l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)

        val1 = 0
        val2 = 0
        temp1 = l1
        temp2 = l2
        i = 0
        while temp1 is not None or temp2 is not None:
            if temp1 is not None:
                val1 += temp1.val * pow(10, i)
                temp1 = temp1.next
            if temp2 is not None:
                val2 += temp2.val * pow(10, i)
                temp2 = temp2.next

            i += 1

        val0 = val1 + val2
        print(val1, val2, val0)

        temp = result
        while val0 > 0:
            temp.val = val0 % 10
            val0 = val0 // 10
            if val0 > 0:
                temp.next = ListNode(0)
                temp = temp.next
        return result

    # 再次优化到一个循环中
    @staticmethod
    def addTwoNumbers3(l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        temp = result
        while l1 is not None or l2 is not None:
            val = temp.val
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            temp.val = val % 10
            if l1 is None and l2 is None and val // 10 == 0:
                break
            temp.next = ListNode(val // 10)
            temp = temp.next
        return result


l10 = ListNode(2)
l11 = ListNode(4)
l10.next = l11
l12 = ListNode(3)
l11.next = l12

l20 = ListNode(5)
l21 = ListNode(6)
l20.next = l21
l22 = ListNode(4)
l21.next = l22

l30 = Solution.addTwoNumbers(l1=l10, l2=l20)
l31 = l30.next
l32 = l31.next

print(l30.val, l31.val, l32.val)


