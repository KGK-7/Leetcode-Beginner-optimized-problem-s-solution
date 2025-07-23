class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(" ")
        return " ".join(words[0:k])

s = Solution()
print(s.truncateSentence("Hello how are you Contestant", 4))  # Output
# "Hello how are you"
print(s.truncateSentence("What is the solution to this problem", 4))  # Output
# "What is the solution"
print(s.truncateSentence("chopper is not a tanuki", 5))  # Output
# "chopper is not a tanuki"