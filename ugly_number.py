def Solution(n):
    if n<=0:
        return False
    factors=[2,3,5]
    for i in factors:
        while n % i == 0:
            n //= i
    return n == 1
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if Solution(n):
        print(f"{n} is a Ugly Number")
    else:
        print(f"{n} is not a Ugly Number")