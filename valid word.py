class Solution(object):
    def isValid(self, word):
        vowels="aeiouAEIOU"
        is_vowel= False
        is_consonant= False

        if len(word)< 3:
            return False
        
        for ch in word:
            if not ch.isalnum():
                return False
            
            if ch.isalpha():
                if ch in vowels:
                    is_vowel = True
                else:
                    is_consonant = True
        
        return is_vowel and is_consonant

s= Solution()
print(s.isValid("hello"))  # True
print(s.isValid("aei"))    # False
print(s.isValid("bcd"))    # False
print(s.isValid("a1b2c3"))  # True