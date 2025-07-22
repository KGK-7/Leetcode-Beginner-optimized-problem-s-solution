class Solution(object):
    def truncateSentence(self, s, k):
        words = list(s.split(" "))
        res = words[0]

        for i in range(1, k):
            res += " " + words[i]
        
        return res

s= Solution()
print(s.truncateSentence("Hello how are you Contestant", 4))  # Output
# "Hello how are you"
print(s.truncateSentence("What is the solution to this problem", 4))  # Output
# "What is the solution"
print(s.truncateSentence("chopper is not a tanuki", 5))  # Output
# "chopper is not a tanuki"