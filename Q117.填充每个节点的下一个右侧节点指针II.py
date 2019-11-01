#!/usr/bin/env python3

# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
# 给定一个二叉树
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 初始状态下，所有 next 指针都被设置为 NULL。
#
# 示例：
# 输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
# 输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
#
# 提示：
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


#         1
#     2         3
#  4     5           6
# 7                     8
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is not None:
            nextNode = None
            temp = root.next
            while temp is not None and nextNode is None:
                if temp.left is not None:
                    nextNode = temp.left
                else:
                    nextNode = temp.right
                temp = temp.next
            if root.right is not None:
                root.right.next = nextNode
                if root.left is not None:
                    root.left.next = root.right
            elif root.left is not None:
                root.left.next = nextNode

            self.connect(root.right)
            self.connect(root.left)

        return root


# n1 = Node(1, None, None, None)
# n2 = Node(2, None, None, None)
# n3 = Node(3, None, None, None)
# n1.left = n2
# n1.right = n3
#
# n4 = Node(4, None, None, None)
# n5 = Node(5, None, None, None)
# n2.left = n4
# n2.right = n5
#
# n7 = Node(7, None, None, None)
# n3.right = n7
#
# n0 = Solution().connect(n1)

#
# t1 = Node(1, None, None, None)
# t2 = Node(2, None, None, None)
# t3 = Node(3, None, None, None)
# t4 = Node(4, None, None, None)
# t5 = Node(5, None, None, None)
# t1.left = t2
# t1.right = t3
# t2.left = t4
# t3.right = t5
# t0 = Solution().connect(t1)
# print(t0.val)


n1 = Node(1, None, None, None)
n2 = Node(2, None, None, None)
n3 = Node(3, None, None, None)
n4 = Node(4, None, None, None)
n5 = Node(5, None, None, None)
n6 = Node(6, None, None, None)
n7 = Node(7, None, None, None)
n8 = Node(8, None, None, None)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
n4.left = n7
n6.right = n8
n0 = Solution().connect(n1)
print(n0.val)
