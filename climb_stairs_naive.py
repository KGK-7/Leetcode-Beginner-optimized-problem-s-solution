def climbStairs(n):
    if n == 1 or n==2:
        return n
    
    return climbStairs(n - 1) + climbStairs(n - 2)

if __name__ == "__main__":
    n = int(input("Enter the number of steps: "))
    print(f"Number of distinct ways to climb {n} steps: {climbStairs(n)}")
# it is a naive recursive solution without memoization
# it has exponential time complexity O(2^n) and space complexity O(n)