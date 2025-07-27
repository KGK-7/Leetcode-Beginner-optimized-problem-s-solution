class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        notes = {}
        for ch in magazine:
            if ch in notes:
                notes[ch] += 1
            else:
                notes[ch] = 1
        
        for ch in ransomNote:
            if ch not in notes or notes[ch] == 0:
                return False
            else:
                notes[ch] -= 1
        
        return True

s= Solution()
# Example usage:
print(s.canConstruct("a", "b"))  # Output: False    
print(s.canConstruct("aa", "ab"))  # Output: False
print(s.canConstruct("aa", "aab"))  # Output: True