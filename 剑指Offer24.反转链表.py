# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
#  
# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#  
# 限制：
# 0 <= 节点个数 <= 5000

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last_node = None
        while head is not None:
            next_node = head.next
            head.next = last_node
            last_node = head
            head = next_node
        return last_node
    
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

t = Solution().reverseList(l1)
while t is not None:
    print(t.val)
    t= t.next