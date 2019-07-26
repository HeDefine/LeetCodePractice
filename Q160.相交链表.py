#!/usr/bin/env python3

# https://leetcode-cn.com/problems/intersection-of-two-linked-lists
# 编写一个程序，找到两个单链表相交的起始节点。
# 示例 1：
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        head1 = headA
        head2 = headB
        while head1 != head2:
            if head1 is not None:
                head1 = head1.next
            else:
                head1 = headB
            if head2 is not None:
                head2 = head2.next
            else:
                head2 = headA
        return head1

# 题解：可以用的方法很多
# 1. 暴力法，遍历每个
# 2. 放到字典里。 两个循环
# 3. 其实我们可以比较容易想到的是，如果两个链表长度相同的话，只需要一个循环，然后找到相同的值就可以了。
# 那么怎么样才能保证两个链表长度相同长度呢，首先你可以遍历两遍，获取两个长度。获取最短的那个长度再开始遍历是一种方法。比较容易的想法
# 另外一种方法就是两个拼接，这样 链表1 = 链表A + 链表B    链表2 = 链表B + 链表A   前面的不去管，后面的才开始判断
