"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

a = 1
b = 20

start = b
factor = b

while factor > 0:
    if start%factor == 0:
        factor -= 1
    else:
        factor = b
        start += b
print start




"""
def findNum(a,b):
    start = b
    factor = b
    
    while factor > 0:
        if start%factor == 0:
            factor -= 1
        start += b
        factor = b
    return start

print findNum(1,10)


"""






"""

def findNum(a,b):
    start = b
    factor = a

    while factor <= b:
        if start%factor == 0:
            print factor
            factor += 1
        print start
        start += 1
    return start

print findNum(1,10)

"""



"""
def findNum(a,b):
    start = b
    nums = range(a,b+1)
    howMany = len(nums)
    yes = 0

    while yes =!= howMany:
        for num in nums:
            if start%num == 0:
                yes += 1
        if yes == nums:
            return start
        else:
            start += 1
            yes = 0


print isDivisible(1,10)

"""


