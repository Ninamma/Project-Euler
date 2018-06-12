"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPallindrome(num):
    return int(str(num)[::-1])-num == 0

def findProduct(a):
    b = a-(a/10)
    c = a - 1
    while c >= b:
        product = a*c
        #print a, c, product
        if isPallindrome(product):
            return product
        else:
            c -= 1
    a -= 1
    c = a-1
    return findProduct(a)
            
print findProduct(99)
print findProduct(999)
print findProduct(9999)
print findProduct(99999)
print findProduct(999999)
