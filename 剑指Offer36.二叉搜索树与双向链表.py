# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
# 要求不能创建任何新的节点，只能调整树中节点指针的指向。
# 
# 为了让您更好地理解问题，以下面的二叉搜索树为例：
#  
#  
# 我们希望将这个二叉搜索树转化为双向循环链表。
# 链表中的每个节点都有一个前驱和后继指针。
# 对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。
# 下图展示了上面的二叉搜索树转化成的链表。
# “head” 表示指向链表中有最小元素的节点。
#  
# 特别地，我们希望可以就地完成转换操作。
# 当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。
# 还需要返回链表中的第一个节点的指针。

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def recursion(node: Node) -> list:
            node_left, node_right = node, node
            if node.left is not None:
                t = recursion(node.left)
                node.left = t[1]
                node.left.right = node
                node_left = t[0]
            if node.right is not None:
                t = recursion(node.right)
                node.right = t[0]
                node.right.left = node
                node_right = t[1]
            
            print(node_left.val, node_right.val)
            return [node_left, node_right]
        res = recursion(root)
        res[0].left = res[1]
        res[1].right = res[0]
        return res[0]

t1 = Node(1)
t2 = Node(2)
t3 = Node(3)
t4 = Node(4)
t5 = Node(5)
t0= Node(0)
t4.left = t2
t4.right = t5
t2.left = t1
t2.right = t3
t1.left = t0

n = Solution().treeToDoublyList(t4)
i = 0
while n is not None and i < 6:
    print('当前:', n.val, '前驱:', n.left.val if n.left is not None else '', '后驱:', n.right.val if n.right is not None else '')
    n = n.right
    i += 1