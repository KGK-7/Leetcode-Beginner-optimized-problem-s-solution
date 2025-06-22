class Solution(object):
    def climbStairs(self, n, memo=None):
        """
        :type n: int
        :rtype: int
        """
        if memo is None:
            memo={}
        
        if n in memo:
            return memo[n]
        
        if n==1 or n==2:
            return n
        
        memo[n]=self.climbStairs(n-1,memo) + self.climbStairs(n-2,memo)
        return memo[n]

# Example usage:
sol = Solution()
print(sol.climbStairs(5))  
print(sol.climbStairs(45))  
