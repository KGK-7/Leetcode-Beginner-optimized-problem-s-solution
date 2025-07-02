class DigitSum:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9

# Example usage
if __name__ == "__main__":
    digit_sum = DigitSum()
    print(digit_sum.addDigits(38))  # Output: 2
    print(digit_sum.addDigits(0))   # Output: 0
    print(digit_sum.addDigits(9))   # Output: 9