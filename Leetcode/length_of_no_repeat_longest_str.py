class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set = []
        left, right, n, count = 0, 0, len(s), 0

        while right < n:
            if s[right] in set:
                count = max(count, right-left)
                while s[left] != s[right]:
                    set.remove(s[left])
                    left += 1

                left += 1
            else:
                set.append(s[right])
            right += 1

        return max(right-left, count)


s = Solution()
print(s.lengthOfLongestSubstring("tmmzuxt"))
