# 请实现 copyRandomList 函数，复制一个复杂链表。
# 在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
# 还有一个 random 指针指向链表中的任意节点或者 null。
#  
# 示例 1：
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
#  
# 示例 2：
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
#  
# 示例 3：
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
#  
# 示例 4：
# 输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
#  
# 提示：
# -10000 <= Node.val <= 10000
# Node.random 为空（null）或指向链表中的节点。
# 节点数目不超过 1000 。
#  

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        t_head = head
        while head is not None:
            node = Node(head.val)
            node.next = head.next
            node.random = head.random
            head.next = node
            head = node.next
        
        if t_head is not None:
            t_head = t_head.next
            res = t_head
            while t_head is not None:
                if t_head.random is not None:
                    t_head.random = t_head.random.next
                if t_head.next is not None:
                    t_head.next = t_head.next.next
                t_head = t_head.next
            return res
        else:
            return None


t = Node(7)
t1 = Node(13)
t2 = Node(11)
t3 = Node(10)
t4 = Node(1)
t.next = t1
t.random = None
t1.next = t2
t1.random = t
t2.next = t3
t2.random = t4
t3.next = t4
t3.random = t2
t4.random = t

q = Solution().copyRandomList(t)
while q is not None:
    print(q.val)
    q = q.next
            
        
        
