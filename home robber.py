class Solution(object):
    def rob(self, nums):
        n = len(nums)

        if n <= 1:
            return nums[0] if n == 1 else 0

        dp = [0]* n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n ):
            dp[i] = max( dp[i-1], nums[i] + dp[i-2])

        return dp[-1]        

s=Solution()
# Example usage:
print(s.rob([1,2,3,1]))  # Output: 4
print(s.rob([2,7,9,3,1]))  # Output: 12
print(s.rob([2,1,1,2]))  # Output: 4
print(s.rob([1,2,3,4,5]))  # Output: 9
