from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        startI, endI, startJ, endJ = 0, m-1, 0, n-1
        res = []

        while True:
            # 左至右
            for j in range(startJ, endJ+1):
                res.append(matrix[startI][j])
            startI += 1
            if startI > endI:
                break
            # 上至下
            for i in range(startI, endI+1):
                res.append(matrix[i][endJ])
            endJ -= 1
            if endJ < startJ:
                break
            # 右至左
            for j in range(endJ, startJ-1, -1):
                res.append(matrix[endI][j])
            endI -= 1
            if endI < startI:
                break
            # 下至上
            for i in range(endI, startI-1, -1):
                res.append(matrix[i][startJ])
            startJ += 1
            if startJ > endJ:
                break
        return res
