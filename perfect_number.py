def isPerfectNumber(num: int) -> bool:
    if num <= 1:
        return False

    total = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            total += i
            nxt_divisor = num // i
            if i != nxt_divisor:
                total += nxt_divisor

    return total == num

if __name__ == "__main__":
    is_perfect = isPerfectNumber(28)
    print(f"Is 28 a perfect number? {is_perfect}")
    is_perfect = isPerfectNumber(6)
    print(f"Is 6 a perfect number? {is_perfect}")
    is_perfect = isPerfectNumber(12)
    print(f"Is 12 a perfect number? {is_perfect}")
    is_perfect = isPerfectNumber(496)
    print(f"Is 496 a perfect number? {is_perfect}")