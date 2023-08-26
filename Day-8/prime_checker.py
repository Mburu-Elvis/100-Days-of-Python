# function to check if a number is a prime number

def is_prime(num):
    x = 1
    while (x <= (num / 2) + 1):
        if num % x == 0 and x != 1:
            print(f"{num} is not prime")
            break
        x += 1
    if (x > (num / 2) + 1):
        print(f"{num} is prime")

for i in range(1, 100):
    is_prime(i)