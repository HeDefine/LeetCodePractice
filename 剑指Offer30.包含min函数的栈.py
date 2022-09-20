# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
#  
# 示例:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.min();   --> 返回 -2.
#  
# 提示：
# 各函数的调用总次数不超过 20000 次


class MinStack:

    def __init__(self):
        self.stack_list = list()
        self.min_stack_list = list()

    def push(self, x: int) -> None:
        self.stack_list.append(x)
        if len(self.min_stack_list) == 0 or x <= self.min_stack_list[-1]:
            self.min_stack_list.append(x)

    def pop(self) -> None:
        val = self.stack_list.pop()
        if val == self.min_stack_list[-1]:
            self.min_stack_list.pop()

    def top(self) -> int:
        return self.stack_list[-1]

    def min(self) -> int:
        return self.min_stack_list[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()