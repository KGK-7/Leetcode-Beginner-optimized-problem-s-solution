class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0]* k for _ in range(k)]
        max_len = 0

        for n in nums:
            rem = n % k
            for j in range(k):
                dp[rem][j] = dp[j][rem] + 1
                max_len = max(max_len, dp[rem][j])
        
        return max_len
