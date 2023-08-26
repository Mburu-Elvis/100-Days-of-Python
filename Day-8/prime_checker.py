# function to check if a number is a prime number

def prime_checker(num):
    iter = 1
    while (iter <= (num / 2) + 1):
        if num % iter == 0 and iter != 1:
            print(f"{num} is not prime")
            break
        iter += 1
    if (iter > (num / 2) + 1):
        print(f"{num} is prime")

# check prime numbers from 1 to 99 
for i in range(1, 100):
    prime_checker(i)