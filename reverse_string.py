def reverseStr(s: str, k: int) -> str:
    result = ''
    for i in range(0, len(s), 2 * k):
        part = s[i:i + 2 * k]          # grab at most 2k characters
        result += part[:k][::-1] + part[k:]  # reverse first k, keep the rest
    return result

# Example usage
s = "abcdefg"
k = 2
print(reverseStr(s, k))  # Output: "bacdfeg"
print(reverseStr("abcdefg", 2))  # Output: "bacdfeg"
print(reverseStr("abcdefghij", 3))  # Output: "cbadefihgj"
