import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []  # 大顶堆，存储较小的
        self.B = []  # 小顶堆，存储较大的

    def addNum(self, num: int) -> None:
        if len(self.A) == len(self.B):
            heapq.heappush(self.B, num)
            heapq.heappush(self.A, -heapq.heappop(self.B))
        else:
            heapq.heappush(self.A, -num)
            heapq.heappush(self.B, -heapq.heappop(self.A))

    def findMedian(self) -> float:
        if len(self.A) == len(self.B):
            return (-self.A[0]+self.B[0])/2
        else:
            return -self.A[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
