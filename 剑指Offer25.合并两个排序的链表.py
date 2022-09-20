# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 限制：
# 0 <= 链表长度 <= 1000

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = None
        last_node = None
        while l1 is not None or l2 is not None:
            if l2 is None or l1 is not None and l1.val <= l2.val:
                min_node = l1
                l1 = l1.next
            elif l1 is None or l2 is not None and l1.val > l2.val:
                min_node = l2
                l2 = l2.next

            if last_node is None:
                last_node = min_node
                res = last_node
            else:
                last_node.next = min_node
                last_node = last_node.next
        return res

l1_0 = ListNode(1)
l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1_0.next = l1_1
l1_1.next = l1_2

l2_0 = ListNode(1)
l2_1 = ListNode(3)
l2_2 = ListNode(4)
l2_0.next = l2_1
l2_1.next = l2_2
                
t = Solution().mergeTwoLists(l1_0, l2_0)
while t is not None:
    print(t.val)
    t= t.next

t = Solution().mergeTwoLists(None, l1_2)
print(t.val)