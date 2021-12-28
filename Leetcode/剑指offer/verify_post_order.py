from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def helper(postorder, start, end):
            if start > end:
                return True

            root = postorder[end]
            k = start
            while k < end and postorder[k] < root:
                k += 1

            # 到此，已经到右子树了
            for i in range(k, end):
                if postorder[i] < root:
                    return False

            # 分别检查左右子树
            return helper(postorder, start, k-1) and helper(postorder, k, end-1)
        return helper(postorder, 0, len(postorder)-1)
