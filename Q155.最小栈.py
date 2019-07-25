#!/usr/bin/env python3

# https://leetcode-cn.com/problems/min-stack
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#


class MinStack:
    def __init__(self):
        self.temp = []
        self.sortTemp = []

    def push(self, x: int) -> None:
        self.temp.append(x)
        if len(self.sortTemp) == 0:
            self.sortTemp.append(x)
            return
        if x <= self.sortTemp[-1]:
            # 比栈顶小的放进去。所以这里有已经排好序了。
            self.sortTemp.append(x)

    def pop(self) -> None:

        v = self.temp.pop(-1)
        if v == self.sortTemp[-1]:
            self.sortTemp.pop(-1)

    def top(self) -> int:
        return self.temp[-1]

    def getMin(self) -> int:
        return self.sortTemp[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
