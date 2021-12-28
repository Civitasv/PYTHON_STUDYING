# -*- coding: utf-8 -*-

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.stack = []

    def push(self, x: int) -> None:
        if not self.min_stack or self.min_stack[len(self.min_stack)-1] > x:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[len(self.min_stack)-1])
        self.stack.append(x)

    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def min(self) -> int:
        return self.min_stack[len(self.min_stack) - 1]
