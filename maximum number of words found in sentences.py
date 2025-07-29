from typing import List
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWords = 0
        for sentence in sentences:
            words = sentence.split()
            maxWords = max(maxWords, len(words))
        return maxWords

s= Solution()
print(s.mostWordsFound(["Hello world", "My name is John", "I love programming"]))  # Example usage
print(s.mostWordsFound(["This is a test", "Another test case", "Short"]))  # Another example usage
print(s.mostWordsFound(["One", "Two three four", "Five six seven eight nine ten"]))  # Yet another example usage