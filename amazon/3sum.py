# Time Complexity = O(n^2)
# Space Complexity = O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, val in enumerate(nums):
            if val > 0:
                break
            if i == 0 or nums[i - 1] != val:
                self.twoSum(nums, i, result)
        return result

    def twoSum(self, nums: List[int], i: int, result: List[List[int]]):
        low, high = i + 1, len(nums) - 1
        while (low < high):
            sum = nums[i] + nums[low] + nums[high]
            if sum < 0:
                low += 1
            elif sum > 0:
                high -= 1
            else:
                result.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
