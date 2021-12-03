# Time Complexity = O(n^2)
# Space Complexity = O(n)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = float('inf')
        nums.sort()
        for i, val in enumerate(nums):
            low, high = i + 1, len(nums) - 1
            while (low < high):
                three_sum = val + nums[low] + nums[high]
                if abs(target - three_sum) < abs(min_diff):
                    min_diff = target - three_sum
                if three_sum < target:
                    low += 1
                else:
                    high -= 1
            if min_diff == 0:
                break
        return target - min_diff
        
