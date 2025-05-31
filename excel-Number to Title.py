class Solution(object):
    def convertToTitle(self, columnNumber):
        result=""
        col=columnNumber

        while col >0:
            col-=1
            rem=col % 26
            result= chr(65 + rem)+ result
            col=col //26
        
        return result 

sol=Solution()
print(sol.convertToTitle(1))    # Output: "A"
print(sol.convertToTitle(28))   # Output: "AB"
print(sol.convertToTitle(701))  # Output: "ZY"
print(sol.convertToTitle(52))   # Output: "AZ"