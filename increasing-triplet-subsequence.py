# Note: this solution only proves *existence* of an increasing triplet subsequence
# If asked to construct the increasing triplet subsequence, this method would not work

# Time Complexity = O(n)
# Space Complexity = O(1)
def increasingTriplet(nums):
    small = big = float('inf')
    for num in nums:
        if num <= small:
            small = num
        elif num <= big:
            big = num
        else:
            return True
    return False