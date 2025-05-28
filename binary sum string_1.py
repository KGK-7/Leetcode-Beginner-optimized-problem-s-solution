class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

# Example usage:
sol = Solution()
print(sol.addBinary("1010", "1011")) 
# This will convert the binary strings to integers, add them, and convert the result back to a binary string.
# Note: The [2:] is used to remove the '0b' prefix that Python adds to binary strings.
# The code defines a class Solution with a method addBinary that takes two binary strings as input,
# converts them to integers, adds them, and returns the result as a binary string.
# The method uses Python's built-in bin function to convert the sum back to a binary string.
# The solution is efficient and concise, leveraging Python's capabilities to handle binary conversions easily.