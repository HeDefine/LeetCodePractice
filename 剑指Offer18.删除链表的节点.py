# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
# 返回删除后的链表的头节点。
# 注意：此题对比原题有改动
#
# 示例 1:
# 输入: head = [4,5,1,9], val = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
#
# 示例 2:
# 输入: head = [4,5,1,9], val = 1
# 输出: [4,5,9]
# 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
#  
# 说明：
# 题目保证链表中节点的值互不相同
# 若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        last_node = ListNode(0)
        first_node = last_node
        while head is not None:
            if head.val != val:
                last_node.next = ListNode(head.val)
                last_node = last_node.next
            head = head.next
        return first_node.next




def printTree(t: ListNode):
    def recursion(o: ListNode):
        if o is not None:
            return [o.val] + recursion(o.next)
        return []
    print(recursion(t))
        
t0 = ListNode(4)
t1 = ListNode(5)
t2 = ListNode(1)
t3 = ListNode(9)
t0.next = t1
t1.next = t2
t2.next = t3

newT0 = Solution().deleteNode(t0, val=1)

printTree(newT0)
