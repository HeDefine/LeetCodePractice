#!/usr/bin/env

# https://leetcode-cn.com/problems/palindrome-linked-list
# 请判断一个链表是否为回文链表。
#
# 示例 1:
# 输入: 1->2
# 输出: false
#
# 示例 2:
# 输入: 1->2->2->1
# 输出: true
#
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l0 = list()
        while head is not None:
            l0.append(head.val)
            head = head.next
        l1 = l0.copy()
        l0.reverse()
        return l0 == l1



