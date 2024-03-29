#!/usr/bin/env python3

# https://leetcode-cn.com/problems/peeking-iterator
# 给定一个迭代器类的接口，接口包含两个方法： next() 和 hasNext()。
# 设计并实现一个支持 peek() 操作的顶端迭代器 -- 其本质就是把原本应由 next() 方法返回的元素 peek() 出来。
#
# 示例:
# 假设迭代器被初始化为列表 [1,2,3]。
# 调用 next() 返回 1，得到列表中的第一个元素。
# 现在调用 peek() 返回 2，下一个元素。在此之后调用 next() 仍然返回 2。
# 最后一次调用 next() 返回 3，末尾元素。在此之后调用 hasNext() 应该返回 false。
#
# 进阶：你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？


class PeekingIterator:
    def __init__(self, iterator):
        self.arr = list()
        while iterator.hasNext():
            self.arr.append(iterator.next())

    def peek(self):
        if self.hasNext():
            return self.arr[0]
        return None

    def next(self):
        return self.arr.pop(0)

    def hasNext(self):
        return len(self.arr) > 0

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
["PeekingIterator","next","peek","next","next","hasNext"]
[[[1,2,3]],[],[],[],[],[]]