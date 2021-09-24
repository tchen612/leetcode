# Time Complexity = O(n)
# Space Complexity = O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, num in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+num)
        return True