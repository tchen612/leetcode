# Time Complexity = O(n^2)
# Space Complexity = O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

# Time Complexity = O(nlog(n))
# Space Complexity = O(n)
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub_seq = []
        for x in nums:
            if len(sub_seq) == 0 or sub_seq[-1] < x:
                sub_seq.append(x)
            else:
                idx = bisect_left(sub_seq, x)
                sub_seq[idx] = x
        return len(sub_seq)