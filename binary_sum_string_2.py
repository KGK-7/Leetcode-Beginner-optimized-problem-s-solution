class Solution(object):
    def addBinary(self, a, b):
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
            
            total=digit_a + digit_b + carry
            digit=total % 2
            carry=total//2

            result=str(digit)+result
            index_a-=1
            index_b-=1
            
        return result

# Example usage:
sol = Solution()
print(sol.addBinary("1010", "1011")) 