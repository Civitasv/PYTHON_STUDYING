from this import d
from time import time
from typing import List
from functools import cmp_to_key


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def helper(x, y):
            return x-y

        # 转换为分钟数
        data = []

        for time in timePoints:
            item = time.split(":")
            data.append(int(item[0])*60 + int(item[1]))

        data.sort(key=cmp_to_key(helper))

        minVal = data[1]-data[0]

        for i in range(1, len(data)):
            minVal = min(minVal, data[i]-data[i-1])

        return min(minVal, data[0]+1440-data[-1])


s = Solution()
print(s.findMinDifference(["23:59", "00:00"]))
