def isDivisible(a,b):
    start = b
    nums = range(a,b+1)
    if all(b%i == 0 for i in nums):
        return b
    else:
        b += 1
        isDivisible(a,b)

print isDivisible(1,10)








