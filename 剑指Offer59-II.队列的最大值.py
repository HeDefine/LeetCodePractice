# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
# 若队列为空，pop_front 和 max_value 需要返回 -1
#
# 示例 1：
# 输入: 
# ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
# [[],[1],[2],[],[],[]]
# 输出: [null,null,null,2,1,2]
# 
# 示例 2：
# 输入: 
# ["MaxQueue","pop_front","max_value"]
# [[],[],[]]
# 输出: [null,-1,-1]
#  
# 限制：
# 1 <= push_back,pop_front,max_value的总操作数 <= 10000
# 1 <= value <= 10^5

from collections import deque
import queue
from typing import Deque
class MaxQueue:

    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        return self.deque[0] if len(self.deque) > 0 else -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)
        print(self.deque, self.queue)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans


# Your MaxQueue object will be instantiated and called as such:
obj = MaxQueue()
param_1 = obj.max_value()
obj.push_back(1)
obj.push_back(5)
obj.push_back(3)
obj.push_back(7)
obj.push_back(6)
param_2 = obj.pop_front()
print(param_2)
print(obj.pop_front())