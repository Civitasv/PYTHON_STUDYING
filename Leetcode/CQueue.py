# -*- coding: utf-8 -*-
class CQueue:

    def __init__(self):
        self.lst1 = []
        self.lst2 = []

    def appendTail(self, value: int) -> None:
        self.lst1.append(value)

    def deleteHead(self) -> int:
        if self.lst1 or self.lst2:
            if self.lst2:
                return self.lst2.pop()
            else:
                while self.lst1:
                    self.lst2.append(self.lst1.pop())
                return self.lst2.pop()
        return -1
