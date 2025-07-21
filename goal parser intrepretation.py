class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        i = 0

        while i < len(command):
            if command[i] == "G":
                result += "G"
                i+= 1
            elif command[i:i+2] == "()":
                result += "o"
                i += 2
            elif command[i:i+4] == "(al)":
                result += "al"
                i += 4
            
        return result

s= Solution()
print(s.interpret("G()(al)"))  # Output: "Goal"
print(s.interpret("G()()()()(al)"))  # Output: "Gooooal"
print(s.interpret("(al)G(al)()()G"))  # Output: "alGalooG"
print(s.interpret("G(al)G(al)G"))  # Output: "GalalG"