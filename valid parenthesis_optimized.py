class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets={ "}":"{", "]":"[", ")": "("}

        for ch in s:
            if ch in brackets.values():
                stack.append(ch)

            elif ch in brackets:
                if not stack or stack[-1]!=brackets[ch]:
                    return False
                stack.pop()

        return not stack

print(Solution().isValid("()"))  
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([)]"))