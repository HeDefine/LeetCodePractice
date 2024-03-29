# 给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。
# 请你返回该链表所表示数字的 十进制值 。
#  
# 示例 1：
# 输入：head = [1,0,1]
# 输出：5
# 解释：二进制数 (101) 转化为十进制数 (5)
#
# 示例 2：
# 输入：head = [0]
# 输出：0
#
# 示例 3：
# 输入：head = [1]
# 输出：1
#
# 示例 4：
# 输入：head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# 输出：18880
#
# 示例 5：
# 输入：head = [0,0]
# 输出：0
#  
# 提示：
# 链表不为空。
# 链表的结点总数不超过 30。
# 每个结点的值不是 0 就是 1。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def recursion(head:ListNode, val:int) -> int:
            if head.next is None:
                return val * 2 + head.val
            return recursion(head.next, val * 2 + head.val)
        return recursion(head, 0)
    
node1 = ListNode(1)
node2 = ListNode(0)
node3 = ListNode(1)
node1.next = node2
node2.next = node3
print(Solution().getDecimalValue(node1))