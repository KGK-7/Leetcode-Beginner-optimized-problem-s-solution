class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words=s.split()

        if len(pattern) != len(s_words):
            return False
        wordMap={}
        mapped_words=set()

        for ch,w in zip(pattern, s_words):
            if ch in wordMap:
                if wordMap[ch] != w:
                    return False
            else:
                if w in mapped_words:
                    return False
                wordMap[ch]=w
                mapped_words.add(w)
        
        return True

sol=Solution()
# Example usage:
sol.wordPattern("abba", "dog cat cat dog")  # Should return True
sol.wordPattern("abba", "dog cat cat fish")  # Should return False      
sol.wordPattern("aaaa", "dog cat cat dog")  # Should return False
sol.wordPattern("abba", "dog dog dog dog")  # Should return False
