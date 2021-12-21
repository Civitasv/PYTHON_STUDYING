from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i, j, w, vi):
            if w == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if vi[i][j]:
                return False

            if board[i][j] == word[w]:
                vi[i][j] = True
                ans = helper(i+1, j, w+1, vi) or helper(i-1, j, w + 1,
                                                        vi) or helper(i, j-1, w+1, vi) or helper(i, j+1, w+1, vi)
                vi[i][j] = False
                return ans
            else:
                return False

        vi = [[False]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, 0, vi):
                    return True
        return False


s = Solution()
print(s.exist(board=[["a"]], word="b"))
