# Time Complexity = O(n)
# Space Complexity = O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        result[0] = 1
        for i in range(1, n):
            result[i] = nums[i - 1] * result[i - 1]
        right = 1;
        for i in reversed(range(n)):
            result[i] = result[i] * right
            right *= nums[i]
        return result
