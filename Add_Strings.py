class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i=len(num1)-1
        j=len(num2)-1
        result=""
        carry=0

        while i>=0 or j>=0 or carry!=0:
            if i>=0:
                n1=ord(num1[i]) - ord('0')
            else:
                n1=0
            if j>=0:
                n2= ord(num2[j]) - ord('0')
            else:
                n2=0
            
            total=n1 + n2 + carry
            digit= total % 10
            carry= total // 10

            result=chr(digit + ord('0'))+ result

            i-=1
            j-=1
        
        return result

# Example usage:
sol = Solution()
print(sol.addStrings("123", "456"))  
print(sol.addStrings("11", "123"))
print(sol.addStrings("0", "0"))  