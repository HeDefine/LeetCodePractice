#!/usr/bin/env python3

# https://leetcode-cn.com/problems/copy-list-with-random-pointer
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
# 要求返回这个链表的深拷贝。 
# 示例：
#
# 输入：
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
#
# 解释：
# 节点 1 的值是 1，它的下一个指针和随机指针都指向节点 2 。
# 节点 2 的值是 2，它的下一个指针指向 null，随机指针指向它自己。
#
# 提示：
# 你必须返回给定头的拷贝作为对克隆列表的引用。


# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        def recursion(n: Node):
            if n is not None:
                if visited.get(n) is not None:
                    return visited[n]
                else:
                    cur = Node(n.val, None, None)
                    visited[n] = cur
                    cur.next = recursion(n.next)
                    cur.random = recursion(n.random)
                    return cur
            return None

        visited = dict()
        res = recursion(head)
        return res


n1 = Node(1, None, None)
n2 = Node(2, None, None)
n1.next = n2
n1.random = n2
n2.next = None
n2.random = n2

n0 = Solution().copyRandomList(n1)
print(n0)
