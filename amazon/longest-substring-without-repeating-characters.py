# Time Complexity = O(n)
# Space Complexity = O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen = {}
        left = 0
        for right, char in enumerate(s):
            if char in seen:
                left = max(seen[char], left)
            max_length = max(max_length, right - left + 1)
            seen[char] = right + 1
        return max_length
