def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            print(f"{num} is not prime")
        print(f"{num} is prime")


is_prime(4)
