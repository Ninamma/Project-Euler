"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

after 2 all prime factors are odd

check if number is odd? if yes, go down by 2 and check if that number is a factor.
Then is it prime.


"""


def isPrime(num):    
    divisor = int(num**0.5) + 1

    while divisor > 2:
        if num%divisor == 0:
            return False
        divisor -= 1
    return True

def findPrimeFactors(num):
    
    max = num
    start = 2
    
    largestPrime = 0

    while start < max: #not sure if i can justify this choice 

        if num%start == 0:

            #finding pairs of factors and checking whether they are prime

            if isPrime(start):
                largestPrime = start

            largerFactor = num/start
            if isPrime(largerFactor):
                return largerFactor
            
            max = largerFactor    
        start += 1
    return largestPrime


print findPrimeFactors(13195)

print findPrimeFactors(600851475143)


"""
def findFactors(num):
    nums = range(2,num+1)
    factors = []
    for i in nums:
        if num%i == 0:
            factors.append(i)
    return factors

def isPrime(lst):
    primeFactors = []

    for i in lst:
        if len(findFactors(i)) == 1:
            primeFactors.append(i)
    return primeFactors

print isPrime(findFactors(600851475143))
"""