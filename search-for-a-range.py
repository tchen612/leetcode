# Time Complexity = O(log(n))
# Space Complexity = O(1))
def searchRange(nums: List[int], target: int) -> List[int]:
    def search(t: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= t:
                high = mid
            else:
                low = mid + 1
        return low

    left = search(target)
    return [left, search(target+1)-1] if target in nums[left:left+1] else [-1, -1]