class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1 
        elif n==2:
            return 2
        first,second=1,2
        step=0

        for i in range(3, n+1):
            step=first+second
            first=second
            second=step
        
        return second

sol=Solution()
print(sol.climbStairs(5))
print(sol.climbStairs(45))
