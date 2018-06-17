"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

"""
# Using isPrime from problem 3
def isPrime(num):    
    divisor = int(num**0.5)

    while divisor > 1:
        if num%divisor == 0:
            return False
        divisor -= 1
    return True

primes = []
start = 2
end = 10001

while len(primes) < end:
    if isPrime(start):
        primes.append(start)
    start += 1
print primes[-1]