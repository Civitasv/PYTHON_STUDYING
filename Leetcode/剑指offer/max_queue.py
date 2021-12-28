from collections import deque


class MaxQueue:

    def __init__(self):
        # a 为普通队列，b 为递减队列
        self.a, self.b = deque(), deque()

    def max_value(self) -> int:
        return -1 if not self.a else self.b[0]

    def push_back(self, value: int) -> None:
        self.a.appendleft(value)
        while self.b and self.b[-1] < value:
            self.b.pop()
        self.b.append(value)

    def pop_front(self) -> int:
        if not self.a:
            return -1
        val = self.a.pop()
        if val == self.b[0]:
            self.b.popleft()
        return val


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
