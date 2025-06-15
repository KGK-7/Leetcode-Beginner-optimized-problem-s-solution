class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result=""
        carry=0
        index_a=len(a)-1
        index_b=len(b)-1

        while index_a >=0 or index_b >=0 or carry!=0:
            if index_a >=0:
                digit_a=int(a[index_a])
            else:
                digit_a=0
            if index_b >=0:
                digit_b=int(b[index_b])
            else:
                digit_b=0
        
            total=digit_a+digit_b+carry
            current_digit=total%2
            carry=total//2

            result=str(current_digit)+result
            index_a-=1
            index_b-=1

        return result

sol=Solution()
# Example usage:
print(sol.addBinary("1010", "1101"))  # Output: "10111"
print(sol.addBinary("11", "1"))      # Output: "100"
print(sol.addBinary("0", "0"))        # Output: "0"
print(sol.addBinary("1", "0"))        # Output: "1"