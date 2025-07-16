class Solution(object):
    def toLowerCase(self, s):
        lower_case=[]

        for ch in s:
            code= ord(ch)

            if 65<= code <=90:
                ch= chr(code + 32)
            lower_case.append(ch)
        
        return ''.join(lower_case)
    
s= Solution()
# Example usage:
print(s.toLowerCase("Hello"))
print(s.toLowerCase("here"))
print(s.toLowerCase("LOVELY"))
