#!/usr/bin/env python3

# https://leetcode-cn.com/problems/clone-graph
# 给定无向连通图中一个节点的引用，返回该图的深拷贝（克隆）。图中的每个节点都包含它的值 val（Int） 和其邻居的列表（list[Node]）。
# 示例：
#    1    -     2
#    |          |
#    4    -     3
# 输入：
# {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
#
# 解释：
# 节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
# 节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
# 节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
# 节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
#  
# 提示：
# 1. 节点数介于 1 到 100 之间。
# 2. 无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
# 3. 由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。
# 4. 必须将给定节点的拷贝作为对克隆图的引用返回。


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        def recursion(n: Node):
            if n is not None:
                cur = Node(n.val, [])
                temp[cur.val] = cur
                for t in n.neighbors:
                    if temp.get(t.val) is None:
                        temp[t.val] = recursion(t)
                    cur.neighbors.append(temp[t.val])
                return cur
        temp = dict()
        return recursion(node)


t1 = Node(1, None)
t2 = Node(2, None)
t3 = Node(3, None)
t4 = Node(4, None)
t1.neighbors = [t2, t4]
t2.neighbors = [t1, t3]
t3.neighbors = [t2, t4]
t4.neighbors = [t1, t3]

t0 = Solution().cloneGraph(t1)
print(t0)
