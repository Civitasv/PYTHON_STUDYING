from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low, hi = 0, len(numbers)-1
        while low <= hi:
            mid = (low+hi)//2
            if numbers[mid] > numbers[hi]:
                low = mid+1
            elif numbers[mid] < numbers[hi]:
                hi = mid
            else:
                hi -= 1
        return numbers[low]


s = Solution()
print(s.minArray([2, 3, 4, 5, 1, 2]))
