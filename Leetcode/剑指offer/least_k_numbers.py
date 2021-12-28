from typing import List
from random import randint


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def partition(arr, start, end):
            k = randint(start, end)
            arr[k], arr[end] = arr[end], arr[k]
            partition = arr[end]

            counter = start

            for i in range(start, end):
                if arr[i] <= partition:
                    arr[i], arr[counter] = arr[counter], arr[i]
                    counter += 1

            arr[end], arr[counter] = arr[counter], arr[end]
            return counter

        def helper(arr, start, end, k):
            if start >= end:
                return
            pos = partition(arr, start, end)

            num = pos-start+1
            if num == k:
                return
            elif num > k:
                helper(arr, start, pos-1, k)
            else:
                helper(arr, pos+1, end, k-num)
        helper(arr, 0, len(arr)-1, k)
        return [arr[x] for x in range(k)]


s = Solution()
print(s.getLeastNumbers([0, 0, 1, 2, 4, 2, 2, 3, 1, 4], 8))
