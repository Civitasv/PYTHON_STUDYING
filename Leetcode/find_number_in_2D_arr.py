from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        def helper(arr, target, low, hi):
            while low <= hi:
                mid = (low+hi)//2
                if arr[mid] >= target:
                    hi = mid-1
                else:
                    low = mid+1
            return low
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])
        if n == 0:
            return False
        for i in range(m):
            index = helper(matrix[i], target, 0, n - 1)
            index = index if index < n else n - 1
            if matrix[i][index] == target:
                return True
            n = index + 1
        return False

    def findNumberIn2DArray2(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False


s = Solution()
print(s.findNumberIn2DArray([[]],
                            20))
