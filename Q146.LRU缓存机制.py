#!/usr/bin/env python3

# https://leetcode-cn.com/problems/lru-cache
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
# 当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
#
# 进阶:
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None


class LRUCache:
    def __init__(self, capacity: int):
        self.maxLength = capacity
        self.nodeDic = dict()
        self.head = None
        self.foot = None

    def __move_to_front__(self, key):
        node = self.nodeDic.get(key)
        if node is not None and node.pre is not None:
            node.pre.next = node.next
            if node.next is None:
                self.foot = node.pre
                self.foot.next = None
            else:
                node.next.pre = node.pre
            node.next = self.head
            node.pre = None
            self.head.pre = node
            self.head = node

    def get(self, key: int) -> int:
        self.__move_to_front__(key)
        node = self.nodeDic.get(key)
        if node is not None:
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.nodeDic.get(key) is not None:
            self.nodeDic[key].value = value
            self.__move_to_front__(key)
        else:
            node = ListNode(key, value)
            self.nodeDic[key] = node
            node.next = self.head
            if self.head:
                self.head.pre = node
            self.head = node
            if self.foot is None:
                self.foot = node
            if len(self.nodeDic) > self.maxLength:
                temp = self.foot
                self.foot = self.foot.pre
                self.foot.next = None
                del self.nodeDic[temp.key]


c = LRUCache(3)
print(c.put(1, 1))  # [1]
print(c.put(2, 2))  # [2,1]
print(c.put(3, 3))  # [3,2,1]
print(c.put(4, 4))  # [4,3,2]
print(c.get(4))  # [4,3,2]
print(c.get(3))  # [3,4,2]
print(c.get(2))  # [2,3,4]
print(c.get(1))  # [2,3,4]
print(c.put(5, 5))  # [5,2,3]
print(c.get(1))  # [5,2,3]
print(c.get(2))  # [2,5,3]
print(c.get(3))  # [3,2,5]
print(c.get(4))  # [3,2,5]
print(c.get(5))  # [5,3,2]
